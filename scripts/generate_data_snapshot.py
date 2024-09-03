import os
import sys
from datetime import datetime
from supabase import create_client, Client
from dotenv import load_dotenv
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Starting script execution...")

# Load environment variables
logger.info("Attempting to load .env file...")
load_dotenv(verbose=True)

# Initialize Supabase client
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_API_KEY")

logger.info(f"SUPABASE_URL found in environment: {'Yes' if url else 'No'}")
logger.info(f"SUPABASE_API_KEY found in environment: {'Yes' if key else 'No'}")

if not url or not key:
    logger.error("Supabase URL or key not found in environment variables.")
    sys.exit(1)

try:
    logger.info("Attempting to create Supabase client...")
    supabase: Client = create_client(url, key)
    logger.info("Successfully created Supabase client.")
except Exception as e:
    logger.error(f"Failed to create Supabase client: {e}")
    sys.exit(1)

def get_table_data(table_name: str):
    """Fetch data from a Supabase table."""
    try:
        logger.info(f"Fetching data from table: {table_name}")
        response = supabase.table(table_name).select("*").limit(5).execute()
        logger.info(f"Response data: {response.data}")
        if not response.data:
            logger.warning(f"No data returned from table {table_name}")
        return response.data
    except Exception as e:
        logger.error(f"Error fetching data from table {table_name}: {e}")
        return []

def get_table_count(table_name: str):
    """Get the total count of records in a table."""
    try:
        logger.info(f"Getting count for table: {table_name}")
        response = supabase.table(table_name).select("*", count="exact").execute()
        count = len(response.data)
        logger.info(f"Count for table {table_name}: {count}")
        return count
    except Exception as e:
        logger.error(f"Error getting count for table {table_name}: {e}")
        return 0

def get_table_fields(table_name: str):
    """Get the field names for a table."""
    data = get_table_data(table_name)
    fields = list(data[0].keys()) if data else []
    logger.info(f"Fields for table {table_name}: {fields}")
    return fields

def generate_table_markdown(table_name: str):
    """Generate Markdown for a single table."""
    logger.info(f"Generating markdown for table: {table_name}")
    data = get_table_data(table_name)
    if not data:
        return f"### {table_name.capitalize()}\nNo data available for this table.\n\n"
    
    count = get_table_count(table_name)
    fields = get_table_fields(table_name)

    markdown = f"### {table_name.capitalize()}\n"
    markdown += f"- Total Records: {count}\n"
    markdown += f"- Fields: {', '.join(fields)}\n"
    markdown += "- Sample Data (first 5 rows):\n\n"

    # Generate table header
    markdown += "| " + " | ".join(fields) + " |\n"
    markdown += "|" + "|".join(["---" for _ in fields]) + "|\n"

    # Generate table rows
    for row in data:
        markdown += "| " + " | ".join(str(row.get(field, "")) for field in fields) + " |\n"

    markdown += "\n"
    return markdown

def generate_data_snapshot():
    """Generate the full DATA_SNAPSHOT.md content."""
    logger.info("Starting to generate data snapshot...")
    tables = ["producers", "brands", "certifications"]
    
    snapshot = f"# Data Snapshot\n\n"
    snapshot += f"This file provides an overview of the current state of data in the Meaningful Bites project database. Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    snapshot += "## Table Summaries\n\n"

    for table in tables:
        snapshot += generate_table_markdown(table)

    snapshot += "## Notes\n"
    snapshot += "- This snapshot represents a sample of the data. For full data access, please refer to the Supabase database.\n"
    snapshot += "- Data is subject to change. Regular updates to this snapshot are recommended.\n"

    logger.info("Finished generating data snapshot.")
    return snapshot

def main():
    try:
        logger.info("Starting main function...")
        snapshot_content = generate_data_snapshot()
        with open("DATA_SNAPSHOT.md", "w") as f:
            f.write(snapshot_content)
        logger.info("DATA_SNAPSHOT.md has been generated successfully.")
    except Exception as e:
        logger.error(f"An error occurred while generating the snapshot: {e}")

if __name__ == "__main__":
    main()