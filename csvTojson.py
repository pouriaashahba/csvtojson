import csv
import json
import os

def make_json(csvFilePath, jsonFilePath):
    data = {}
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        for rows in csvReader:
            key = rows['firstName']
            data[key] = rows
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4, ensure_ascii=False))

csvFilePath = input("Enter CSV file path: ").strip()
jsonFilePath = input("Enter JSON output path: ").strip()

if not csvFilePath or not os.path.isfile(csvFilePath):
    print("⚠️ CSV file not found or invalid path.")
else:
    if not jsonFilePath:
        print("⚠️ Invalid JSON output path.")
    else:
        try:
            make_json(csvFilePath, jsonFilePath)
            print(f"✅ JSON file created: {jsonFilePath}")
        except Exception as e:
            print(f"⚠️ Error: {e}")

