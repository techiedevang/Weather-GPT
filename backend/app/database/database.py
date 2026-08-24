import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

def get_supabase_client() -> Client:
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_ANON_KEY")
    
    # Return a dummy client or None if not configured, to allow local dev without DB
    if not url or not key:
        return None
        
    return create_client(url, key)
