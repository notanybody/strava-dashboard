from datetime import datetime, timezone
def get_yearly_mileage(runs):
    current_year = datetime.now().year 
    total = sum(
        float(run.distance) / 1609
        for run in runs
        if run.start_date.year == current_year
    )
    return round (total, 2)

def get_longest_run(runs):
    longest = max(runs, key=lambda run: float(run.distance))
    return round(float(longest.distance) / 1609, 2)

def get_average_pace(runs):
    paces = []
    for run in runs:
        if run.moving_time and float(run.distance) > 0:
            minutes = float(run.moving_time) / 60
            miles = float(run.distance) / 1609
            paces.append(minutes / miles)
    avg = sum(paces) / len(paces)
    mins = int(avg)
    secs = int((avg - mins) * 60)
    return f"{mins}:{secs:02d} /mi"

def get_weekly_mileage(runs):
    weeks = {}
    for run in runs:
        week = run.start_date.isocalendar()[1]
        year = run.start_date.year
        key = f"{year}-W{week:02d}"
        miles = float(run.distance) / 1609
        weeks[key] = weeks.get(key, 0) + miles
    
    sorted_weeks = sorted(weeks.items())[-12:]
    return [(week, round(miles, 1)) for week, miles in sorted_weeks]
