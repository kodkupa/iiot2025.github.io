import pandas as pd
import json
import os
import re
import asyncio
import aiohttp
import aiofiles
from urllib.parse import urlparse, parse_qs
from PIL import Image
import imageio.v3 as iio
import numpy as np
import unicodedata

sem = asyncio.Semaphore(10)

def sanitize_filename(name):
    # Normalize and strip accents
    name = unicodedata.normalize('NFKD', name)
    name = ''.join(c for c in name if not unicodedata.combining(c))

    # Replace spaces with underscores
    name = re.sub(r'\s+', '_', name)

    # Remove any non-alphanumeric character except underscore and hyphen
    name = re.sub(r'[^\w\-]', '', name)

    return name.strip()


# Function to map content types to file extensions
def extension_from_content_type(content_type, content_disposition, member_name):
    mapping = {
        'image/jpeg': '.jpg',
        'image/png': '.png',
        'image/webp': '.webp',
        'image/heic': '.heic',
        'image/heif': '.heif'
    }

    if "image" in content_type.lower():
        if content_type in mapping:
            return mapping[content_type]
        else:
            print(f"[WARN] {member_name} - Unsupported image content type: {content_type}")
            return None
    else:
        if "filename=" in content_disposition:
            filename = content_disposition.split("filename=")[-1].strip('"')
            ext = os.path.splitext(filename)[1]
            return ext.lower()
        else:
            print(f"[FAIL] {member_name} - Could not determine file extension from Content-Type or Content-Disposition")
            return None


# Function to convert HEIC to JPG or PNG using Pillow and pillow-heif
async def convert_heic_to_jpg(heic_data, save_path):
    try:
        # Decode image bytes with imageio
        img_array = iio.imread(heic_data, extension=".heic")
        img = Image.fromarray(img_array)
        img.save(save_path, format="JPEG")
        print(f"[DONE] Converted and saved as {save_path}")
    except Exception as e:
        print(f"[ERROR] Failed to convert HEIC image - {e}")


# Main function to download images and handle conversion if necessary
async def download_image(session, url, save_base_path, member_name):
    async with sem:
        try:
            # Parse the URL to retrieve the file ID if it's a Google Drive link
            parsed = urlparse(url)
            query_params = parse_qs(parsed.query)
            file_id = query_params.get("id", [None])[0]
            if file_id:
                url = f"https://drive.google.com/uc?export=download&id={file_id}"
            else:
                print(f"[SKIP] Invalid Google Drive URL: {url}")
                return None

            async with session.get(url) as resp:
                content_type = resp.headers.get("Content-Type", "")
                content_disposition = resp.headers.get("Content-Disposition", "")

                # Determine the file extension based on Content-Type and Content-Disposition
                ext = extension_from_content_type(content_type, content_disposition, member_name)

                if not ext:
                    print(f"[FAIL] {member_name} - Could not determine extension, skipping...")
                    return None

                # Prepare the save path with the determined extension
                save_path = f"{save_base_path}{ext}"

                # If it's HEIC, we'll convert to JPG instead, so check for the JPG file
                if ext == ".heic":
                    converted_path = f"{save_base_path}.jpg"
                    if os.path.exists(converted_path):
                        print(f"[SKIP] Exists (converted): {member_name} → {converted_path}")
                        return os.path.basename(converted_path)
                else:
                    if os.path.exists(save_path):
                        print(f"[SKIP] Exists: {member_name} → {save_path}")
                        return os.path.basename(save_path)


                # Download the image if the status is 200 (OK)
                if resp.status == 200:
                    if ext == ".heic":
                        # If HEIC image, convert it to JPG
                        heic_data = await resp.read()
                        save_path_jpg = f"{save_base_path}.jpg"
                        await convert_heic_to_jpg(heic_data, save_path_jpg)
                        return os.path.basename(save_path_jpg)
                    else:
                        # Save the image as-is
                        async with aiofiles.open(save_path, 'wb') as f:
                            await f.write(await resp.read())
                        print(f"[DONE] Downloaded {member_name} as {save_path}")
                        return os.path.basename(save_path)
                else:
                    print(f"[FAIL] {member_name} - Invalid image content (status {resp.status})")
                    return None
        except Exception as e:
            print(f"[ERROR] {member_name} - {e}")
            return None

async def download_all_images(image_tasks):
    failed_images = []
    updated_image_map = {}

    async with aiohttp.ClientSession() as session:
        tasks = [
            download_image(session, url, base_path, member_name)
            for url, base_path, member_name in image_tasks
        ]
        results = await asyncio.gather(*tasks)

    for result, (_, _, member_name) in zip(results, image_tasks):
        if result:
            updated_image_map[member_name] = result
        else:
            failed_images.append(member_name)

    return updated_image_map, failed_images

def load_and_extract(csv_path, image_dir="images"):
    df = pd.read_csv(csv_path, delimiter=',')
    df.columns = df.columns.str.strip()

    output = {"regular": [], "guest": []}
    countries = set()
    schools = set()
    image_tasks = []
    member_picture_lookup = {}

    os.makedirs(image_dir, exist_ok=True)

    for _, row in df.iterrows():
        team = {
            "name": row["Team Name"].strip(),
            "school": row["School/Organization"].strip(),
            "country": row["Country"].strip(),
            "members": []
        }

        countries.add(team["country"])
        schools.add(team["school"])

        for i in range(5):
            suffix = "" if i == 0 else f".{i}"
            given_col = f"Given name{suffix}"
            family_col = f"Family name{suffix}"
            picture_col = f"Picture{suffix}"

            given = row.get(given_col, '')
            family = row.get(family_col, '')
            picture_url = row.get(picture_col, '')

            # Skip if all fields are missing or NaN
            if all(pd.isna(x) or str(x).strip().lower() == "nan" or str(x).strip() == "" for x in [given, family, picture_url]):
                continue

            # Now safely convert to strings
            given = str(given).strip()
            family = str(family).strip()
            picture_url = str(picture_url).strip()
            
            full_name = f"{given} {family}".strip()
            filename_base = sanitize_filename(full_name)
            base_path = os.path.join(image_dir, filename_base)

            if picture_url:
                image_tasks.append((picture_url, base_path, full_name))

            member_picture_lookup[full_name] = ""

            member = {
                "firstName": given,
                "lastName": family,
                "picture": "",  # placeholder
                "role": "Leader" if i == 4 else "Contestant"
            }

            team["members"].append(member)


        if row["Qualification type"].strip() == "Guest team":
            output["guest"].append(team)
        else:
            output["regular"].append(team)

    return output, countries, schools, image_tasks, member_picture_lookup

def update_team_pictures(output, picture_lookup):
    for group in ["regular", "guest"]:
        for team in output[group]:
            for member in team["members"]:
                name = f"{member['firstName']} {member['lastName']}".strip()
                if name in picture_lookup:
                    member["picture"] = picture_lookup[name]

def print_field_info(countries, schools):
    print("\n--- Field Information ---")
    print("Countries:")
    for country in sorted(countries):
        print(f"- {country}")

    print("\nSchools/Organizations:")
    for school in sorted(schools):
        print(f"- {school}")

if __name__ == "__main__":
    csv_file = "src/lib/json-data/teams.csv"
    json_output_file = "src/lib/json-data/teams.json"
    image_output_dir = "static\\images\\participants"

    teams_json, countries, schools, image_tasks, picture_lookup = load_and_extract(csv_file, image_output_dir)

    print(f"\n⬇️  Downloading {len(image_tasks)} images...")
    updated_picture_map, failed_images = asyncio.run(download_all_images(image_tasks))

    # Update picture references in teams_json
    picture_lookup.update(updated_picture_map)
    update_team_pictures(teams_json, picture_lookup)

    with open(json_output_file, "w", encoding="utf-8") as f:
        json.dump(teams_json, f, ensure_ascii=False, indent=4)
    print(f"\n✅ Written {json_output_file}")

    print_field_info(countries, schools)

    if failed_images:
        print("\n--- Participants without images ---")
        for name in failed_images:
            print(f"- {name}")
    else:
        print("\n✅ All images downloaded successfully.")
