from stravalib.client import Client
def get_runs(client, limit=100):
    activities = client.get_activities(limit=limit)
    runs = [a for a in activities if a.type == "Run"]
    return runs

def print_runs(runs):
    for run in runs:
        print(f"{run.start_date_local.date()} - {run.name} - {float(run.distance) / 1609:.2f} mi")
