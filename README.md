# CSV to JSON Converter

This Python script converts a CSV file to a JSON file.  
It uses the `firstName` column as the key for each record.

---

## Requirements

No external packages are required.  
All modules (`csv`, `json`, `os`) are part of the Python standard library.

---

## Usage

Run the script:

```bash
python3 csvTojson.py
```
---

It will prompt you to enter:

1.The path to the CSV file
2.The path for the output JSON file

Enter CSV file path: sample_names.csv
Enter JSON output path: myfile.json

The script will generate a JSON file at the specified location.

## Notes
Make sure your CSV file has a column named firstName.

The output JSON will have the firstName as the key for each record.

The script handles file path errors and will notify if the CSV file doesn't exist.
