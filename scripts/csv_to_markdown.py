import csv
from datetime import datetime
import sys

def csv_to_markdown(csv_file, md_file):
    try:
        with open(csv_file, 'r') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)  # Read the first row as headers
            print("CSV Headers:", headers)

            # Identify the indices of important columns
            table_name_index = headers.index('table_name') if 'table_name' in headers else -1
            column_name_index = headers.index('column_name') if 'column_name' in headers else -1
            data_type_index = headers.index('data_type') if 'data_type' in headers else -1
            is_nullable_index = headers.index('is_nullable') if 'is_nullable' in headers else -1
            column_default_index = headers.index('column_default') if 'column_default' in headers else -1

            if table_name_index == -1 or column_name_index == -1:
                print("Error: CSV must contain at least 'table_name' and 'column_name' columns")
                return

            with open(md_file, 'w') as mdfile:
                mdfile.write(f"# Database Schema\n\n")
                mdfile.write(f"Last updated: {datetime.now().strftime('%Y-%m-%d')}\n\n")

                current_table = None
                for row in reader:
                    table_name = row[table_name_index]
                    column_name = row[column_name_index]

                    if table_name != current_table:
                        if current_table:
                            mdfile.write("\n")
                        current_table = table_name
                        mdfile.write(f"## Table: {current_table}\n\n")
                        mdfile.write("| Column Name | Data Type | Nullable | Default | Description |\n")
                        mdfile.write("|-------------|-----------|----------|---------|-------------|\n")

                    data_type = row[data_type_index] if data_type_index != -1 else 'N/A'
                    is_nullable = row[is_nullable_index] if is_nullable_index != -1 else 'N/A'
                    column_default = row[column_default_index] if column_default_index != -1 else 'NULL'

                    mdfile.write(f"| {column_name} | {data_type} | "
                                 f"{is_nullable} | {column_default} | |\n")

                mdfile.write("\n## Relationships\n\n- [Add relationships here]\n\n")
                mdfile.write("## Indexes\n\n- [Add indexes here]\n\n")
                mdfile.write("## Notes\n\n- [Add any additional notes about the schema here]\n")

        print(f"Successfully created {md_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script_name.py <input_csv_file> <output_md_file>")
        sys.exit(1)
    
    input_csv = sys.argv[1]
    output_md = sys.argv[2]
    csv_to_markdown(input_csv, output_md)