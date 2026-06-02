from dotenv import load_dotenv
from auth import get_client
from activities import get_runs, print_runs
from stats import get_yearly_mileage, get_longest_run, get_average_pace

load_dotenv()

client = get_client()
athlete = client.get_athlete()

print(f"Authenticated as: {athlete.firstname} {athlete.lastname}")

runs = get_runs(client)

from stats import get_weekly_mileage 
weekly = get_weekly_mileage(runs)
for week, miles in weekly:
    print(f"{week}: {miles} mi")

print(f"Yearly mileage: {get_yearly_mileage(runs)} mi")
print(f"Longest run: {get_longest_run(runs)} mi")
print(f"Average pace: {get_average_pace(runs)}")
