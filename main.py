from dotenv import load_dotenv
from auth import get_client
from activities import get_runs, print_runs
from stats import get_yearly_mileage, get_longest_run, get_average_pace, get_weekly_mileage
from dashboard import StravaApp

import logging
logging.getLogger("stravalib").setLevel(logging.ERROR)

load_dotenv()

client = get_client()
runs = get_runs(client)
athlete = client.get_athlete()

stats = {
    "yearly_mileage": f"{get_yearly_mileage(runs)} mi",
    "longest run": f"{get_longest_run(runs)} mi",
    "avg_pace": get_average_pace(runs)
}

weekly_data = get_weekly_mileage(runs)

app = StravaApp(stats=stats, weekly_data=weekly_data)
app.run()
