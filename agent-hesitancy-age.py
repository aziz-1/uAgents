from uagents import Agent, Context, Model
import requests
import pandas as pd


class SupabaseRequest(Model):
    """Model for requesting data from Supabase"""
    table_name: str


class SupabaseResponse(Model):
    """Model for receiving data from Supabase"""
    data: list


AGENT_MAILBOX_KEY = "96da9c0c-3eb0-4b9c-8f1f-fa42576e1b80"
SEED_PHRASE = "asishugugjhtifkjfhtefmulgvgnytdhg"

# Now your agent is ready to join the agentverse!
agent = Agent(
    name="alice",
    seed=SEED_PHRASE,
    mailbox=f"{AGENT_MAILBOX_KEY}@https://agentverse.ai"
)

print(agent.address)

SUPABASE_URL = "https://kmyjfzgkltzglviijnub.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtteWpmemdrbHR6Z2x2aWlqbnViIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzI5ODY0ODUsImV4cCI6MjA0ODU2MjQ4NX0.MA2J85nb1KA0Yq87OvJcXhQhdtmvdRx8hQJ1eqASoQA"
TABLE_NAME = "v_hesitancy_age"


@agent.on_event("startup")
async def fetch_data(ctx: Context):
    """Fetch data from Supabase when the agent starts"""
    # Build the request
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
    }
    response = requests.get(f"{SUPABASE_URL}/rest/v1/{TABLE_NAME}", headers=headers)

    if response.status_code == 200:
        data = response.json()
        ctx.logger.info(f"Data successfully fetched from Supabase: {len(data)} rows")
        df = pd.DataFrame(data)
        ctx.logger.info(f"Sample data:\n{df.head()}")
    else:
        ctx.logger.error(f"Error fetching data: {response.status_code}, {response.text}")


if __name__ == "__main__":
    agent.run()
