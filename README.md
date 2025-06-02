
# iiot2025.github.io

This is the official website for the 2025 Budapest Finals of the International Informatics Olympiad in Teams.


## Run Locally

Clone the project:
```bash
  git clone https://github.com/kodkupa/iiot2025.github.io
```

Install dependencies:
```bash
  cd iiot2025.github.io
```
```bash
  npm install
```

Run the project locally:

```bash
  npm run dev
```


## Deployment

To deploy on github pages, run:

```
  npm run deploy
```


## Participants

The participants and teams are stored in the `src/lib/json-data/teams.json` file, in the given format, extend if necessary.
Pictures of the participants are stored at `static/images/participants`.


## Schedule

The schedule table is downloaded as a comma separated csv file from google sheets and stored at `src/lib/Program.html`, it can be easily replaced this way.


## Documents

The documents that are linked on the site such as the *privacy_policy.pdf* etc. are in the `static/documents` folder, replace them there if needed.


## Update Results

The data for the results pages is stored in the `results.json` file in the `src/lib/json-data` folder.

Create the results table in Excel, you can find an example file at [static/excel/results.xlsx](static/excel/results.xlsx) with the correct format. 

If you want to display the awarded medals, create a column named `Award`. There are three available values in this column: `gold`, `silver` and `bronze`. If the team didn't get any award, leave the corresponding cell empty.

The rest of the columns header names should match the example format.

After that, use an [Excel to JSON converter](https://tableconvert.com/excel-to-json) to convert it into an **Array of Object*** format. 

*(On the linked site, choose the *Array of Object* option for the JSON format.)

(You can also check the data in the `results.json` file for the required final JSON format.)


## Authors

| Github | Email |
| :- | :- |
| [@TkcsHnr](https://www.github.com/TkcsHnr) | [tkcshnr@gmail.com](mailto:tkcshnr@gmail.com) |
| [@niklaci](https://www.github.com/niklaci) | [laszlo.nikhazy@gmail.com](mailto:laszlo.nikhazy@gmail.com) |


## Color Reference

| Color             | Hex                                                                |
| ----------------- | ------------------------------------------------------------------ |
| IIOT logo turquoise | ![#6dc1c3](https://placehold.co/15x15/6dc1c3/6dc1c3.png) `#6dc1c3` |
| IIOT logo purple | ![#f8f8f8](https://placehold.co/15x15/595bb4/595bb4.png) `#595bb4` |
| IIOT logo grey | ![#00b48a](https://placehold.co/15x15/a3a3a3/a3a3a3.png) `#a3a3a3` |



