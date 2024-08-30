import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment variables
load_dotenv()

# Initialize Supabase client
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_API_KEY")
supabase: Client = create_client(url, key)

def test_connection():
    try:
        # Try to fetch a row from a non-existent table
        response = supabase.table('test').select("*").limit(1).execute()
        print("Connected to Supabase successfully!")
    except Exception as e:
        print(f"Failed to connect to Supabase: {str(e)}")

if __name__ == "__main__":
    test_connection()