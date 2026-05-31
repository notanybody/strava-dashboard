from dotenv import load_dotenv
import os

load_dotenv()

client_id = os.getenv("STRAVA_CLIENT_ID")
client_secret = os.getenv("STRAVA_CLIENT_SECRET")

print(f"Client ID: {client_id}")
print(f"Client secret loaded: {client_secret is not None}")
