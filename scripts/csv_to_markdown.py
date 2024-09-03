import csv
from datetime import datetime
import sys

def csv_to_markdown(csv_file, md_file):
    try:
        with open(csv_file, 'r') as csvfile, open(md_file, 'w') as mdfile:
            reader = csv.DictReader(csvfile)
            current_table = None

            mdfile.write(f"# Database Schema\n\n")
            mdfile.write(f"Last updated: {datetime.now().strftime('%Y-%m-%d')}\n\n")

            for row in reader:
                if 'table_name' not in row or 'column_name' not in row:
                    print(f"Warning: CSV file doesn't have expected column names. Current row: {row}")
                    continue

                if row['table_name'] != current_table:
                    if current_table:
                        mdfile.write("\n")
                    current_table = row['table_name']
                    mdfile.write(f"## Table: {current_table}\n\n")
                    mdfile.write("| Column Name | Data Type | Nullable | Default | Description |\n")
                    mdfile.write("|-------------|-----------|----------|---------|-------------|\n")

                mdfile.write(f"| {row['column_name']} | {row.get('data_type', 'N/A')} | "
                             f"{'YES' if row.get('is_nullable') == 'YES' else 'NO'} | "
                             f"{row.get('column_default', 'NULL')} | |\n")

            mdfile.write("\n## Relationships\n\n- [Add relationships here]\n\n")
            mdfile.write("## Indexes\n\n- [Add indexes here]\n\n")
            mdfile.write("## Notes\n\n- [Add any additional notes about the schema here]\n")

        print(f"Successfully created {md_file}")
    except FileNotFoundError:
        print(f"Error: Could not find the file {csv_file}")
    except PermissionError:
        print(f"Error: Do not have permission to read {csv_file} or write to {md_file}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script_name.py <input_csv_file> <output_md_file>")
        sys.exit(1)
    
    input_csv = sys.argv[1]
    output_md = sys.argv[2]
    csv_to_markdown(input_csv, output_md)