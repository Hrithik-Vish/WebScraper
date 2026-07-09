# The Target: supabase.table("table_name")

# The Action: .select(), .insert(), .update(), or .delete()

# The Filters (Optional): .eq(), .gt(), .ilike(), etc. (Who are we affecting?)

# The Modifiers (Optional): .order(), .limit(), .single(), etc. (How should the data look?)

# The Trigger: .execute() (Send it to the server!)


import os
import time
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()
url = os.getenv("SUPABASE_URL")
public_key = os.getenv("SUPABASE_PUBLISHABLE_KEY")
secret_key = os.getenv("SUPABASE_SECRET_KEY")

if not url or not public_key or not secret_key:
    raise ValueError("either url or public_key or secret_key does not exists in .env or there is a typo in code")

supabase: Client = create_client (url, secret_key)


def fetch_websites():
    max_attempts = 3

    for attempt in range(1, max_attempts +1):
        print(f"fetching websites, attempt: {attempt}")

        try:
            read_websites = (
                supabase.table("websites").select("id, web_domain_name").execute()
            )
            if read_websites.data:
                websites_list = read_websites.data
                return websites_list
            else:
                print("data fetched was empty")
                return

        except Exception as e:
            if attempt < max_attempts:
                print(f"attempt: {attempt} failed due to exception: {e}, trying again")
                time.sleep(5)
            else:
                print(f"attempt: {attempt} failed,\nall attempts failed, try again later, exception: {e}")




    


def fetch_novels(site_id):
    max_attempts = 2

    for attempt in range(1, max_attempts +1):
        print(f"fetching novels, attempt: {attempt}")

        try:
            read_novels = (
                supabase.table("novels").select("*").eq("web_id", site_id).execute()
            )
            if read_novels.data:
                novels_list = read_novels.data
                return novels_list
            else:
                print("data fetched was empty")
                return

        except Exception as e:
            if attempt < max_attempts:
                print(f"attempt: {attempt} failed due to exception: {e}, trying again")
                time.sleep(5)
            else:
                print(f"attempt: {attempt} failed,\nall attempts failed, try again later, exception: {e}")

