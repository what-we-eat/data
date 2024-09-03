import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment variables
load_dotenv()

# Initialize Supabase client
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_API_KEY")

def test_connection():
    if not url or not key:
        print("Error: Supabase URL or API key not found in environment variables.")
        return

    try:
        supabase: Client = create_client(url, key)
        print("Successfully created Supabase client.")

        # Try to fetch a row from the 'producers' table
        response = supabase.table('producers').select("*").limit(1).execute()
        print("Successfully queried 'producers' table.")
        print(f"Sample data: {response.data}")

        # If we get here, it means both connection and query were successful
        print("Connected to Supabase and verified data access successfully!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        print("Please check your Supabase URL, API key, and ensure the 'producers' table exists.")

if __name__ == "__main__":
    test_connection()