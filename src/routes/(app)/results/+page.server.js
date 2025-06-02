// @ts-nocheck
import results from '$lib/json-data/results.json';

export async function load() {
    const rows = results;
    
    const hasTasks = false;
    
    const main_rows = rows['main'];
    let guest_rows = rows['guest'];
    
    const headers = Object.keys(main_rows[0]);

    return { headers, main_rows, guest_rows, hasTasks };
};