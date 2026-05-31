from dotenv import load_dotenv
from auth import get_client

load_dotenv()

client = get_client()
athlete = client.get_athlete()

print(f"Authenticated as: {athlete.firstname} {athlete.lastname}")
