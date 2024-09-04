import os
import json
import csv
from datetime import datetime
from supabase import create_client, Client

# Initialize Supabase client
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

def update_snapshot():
    # Fetch all table names in the public schema
    response = supabase.rpc('get_public_tables').execute()
    
    if hasattr(response, 'error') and response.error is not None:
        raise Exception(f"Error fetching tables: {response.error}")
    
    tables = response.data

    # Ensure the directory exists
    os.makedirs('public_data/snapshots/latest', exist_ok=True)

    for table in tables:
        # Fetch data from Supabase
        response = supabase.table(table).select("*").execute()
        data = response.data

        # Write the updated data to a CSV file
        with open(f'public_data/snapshots/latest/{table}.csv', 'w', newline='') as f:
            if data:
                writer = csv.DictWriter(f, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)

    # Update metadata
    metadata = {
        'last_updated': datetime.now().isoformat(),
        'table_record_counts': {table: len(supabase.table(table).select("*").execute().data) for table in tables}
    }
    with open('public_data/snapshots/latest/metadata.json', 'w') as f:
        json.dump(metadata, f, indent=2)

if __name__ == "__main__":
    update_snapshot()