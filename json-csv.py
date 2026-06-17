import json
import csv
import os

OUTPUT_FILE = "bodies.csv"

folders = {
    "genz2": "0",
    "millennials2": "1",
    "genx2": "2",
    "boomeri2": "3"
}

with open(OUTPUT_FILE, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["body", "gen"])
    for folder, gen in folders.items():
        for i in range(1, 21):
            INPUT_FILE = f"{folder}/comments ({i}).json"

            if not os.path.isfile(INPUT_FILE):
                print(f"Skipping {INPUT_FILE}, nav faila")
                continue

            with open(INPUT_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)

            if isinstance(data, dict):
                data = [data]

            # noņem line breaks, atrod un saglabā tikai "body" kur ir komentāra teksts
            bodies = [item["body"].replace("\n", "").replace("\r", "") for item in data if "body" in item]

            for text in bodies:
                writer.writerow([text, gen])

# print(f"{len(bodies)} ieraksti → {OUTPUT_FILE}")