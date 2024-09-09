import os
import csv
import json
import sys
from collections import defaultdict

# Increase the CSV field size limit
csv.field_size_limit(sys.maxsize)

def csv_to_json(csv_file_path):
    data = []
    try:
        with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data.append(row)
        return data
    except Exception as e:
        print(f"Error processing file {csv_file_path}: {str(e)}")
        return None

def generate_data_snapshot(csv_directory, output_file):
    print(f"Current working directory: {os.getcwd()}")
    print(f"Attempting to access directory: {os.path.abspath(csv_directory)}")
    
    if not os.path.exists(csv_directory):
        print(f"Error: The directory {csv_directory} does not exist.")
        return

    snapshot = defaultdict(list)
    
    for filename in os.listdir(csv_directory):
        if filename.endswith('.csv'):
            table_name = os.path.splitext(filename)[0]
            file_path = os.path.join(csv_directory, filename)
            print(f"Processing file: {file_path}")
            data = csv_to_json(file_path)
            if data is not None:
                snapshot[table_name] = data
            else:
                print(f"Skipping file due to error: {filename}")
    
    # Create the 'json' subdirectory if it doesn't exist
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(dict(snapshot), json_file, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    csv_directory = os.path.join("..", "public_data", "snapshots", "latest")
    # Place the output file in a 'json' subdirectory
    output_file = os.path.join(csv_directory, "json", "DATA_SNAPSHOT.json")
    generate_data_snapshot(csv_directory, output_file)
    print(f"Data snapshot generated: {output_file}")