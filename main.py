from dotenv import load_dotenv
from auth import get_client
from activities import get_runs, print_runs

load_dotenv()

client = get_client()
athlete = client.get_athlete()

print(f"Authenticated as: {athlete.firstname} {athlete.lastname}")

runs = get_runs(client)
print_runs(runs)
