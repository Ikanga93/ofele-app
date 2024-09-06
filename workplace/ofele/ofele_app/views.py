import random
from datetime import datetime, timedelta
from django.shortcuts import render

# List of members
members = [
    'Papa Onesime', 'Papa Jeremie', 'Maman Bijou', 'Papa Yves', 'Maman Alphie',
    'Maman Caro', 'Maman Sandrine', 'Papa Chris', 'Maman Mado', 'Maman Olga',
    'Maman Hadassa', 'Ma Meme', 'Ma Gisele', 'Frère Jeantiny'
]

# Fixed schedule for Monday and Saturday prayers
monday_schedule = [
    ("Papa Onesime", "15 July"),
    ("Papa Jeremie", "22 July"),
    ("Maman Bijou", "29 July"),
    ("Papa Yves", "05 August"),
    ("Maman Alphie", "12 August"),
    ("Maman Caro", "19 August"),
    ("Maman Sandrine", "26 August"),
    ("Papa Chris", "02 September"),
    ("Maman Mado", "09 September"),
    ("Maman Olga", "16 September"),
    ("Maman Hadassa", "23 September"),
]

saturday_schedule = [
    ("Maman Mado", "13 July"),
    ("Maman Caro", "20 July"),
    ("Papa Jeremie", "27 July"),
    ("Papa Chris", "03 August"),
    ("Ma Meme", "10 August"),
    ("Ma Gisele", "17 August"),
    ("Frère Jeantiny", "24 August"),
    ("Papa Onezime", "31 August"),
    ("Ma Alphie", "07 September"),
    ("Papa Yves", "14 September"),
    ("Maman Olga", "21 September"),
    ("Maman Bijou", "28 September"),
    ("Maman Sandrine", "05 October"),
    ("Maman Hadassa", "12 October"),
]

def create_weekly_prayer_teams(members):
    """Create new pairs of members for each week."""
    random.shuffle(members)
    prayer_teams = [(members[i], members[i + 1]) for i in range(0, len(members) - 1, 2)]
    
    if len(members) % 2 != 0:
        prayer_teams.append((members[-1], "No Pair"))

    return prayer_teams

def get_current_week_start_date():
    """Get the start date of the current week (Monday)."""
    today = datetime.now()
    start_date = today - timedelta(days=today.weekday())
    return start_date

def moderation_schedule(request):
    # Get the start date of the current week
    start_date = get_current_week_start_date()
    
    # Generate prayer teams for the current week
    prayer_teams = create_weekly_prayer_teams(members)

    # Convert schedule dates to include the current week for the view
    monday_dates = [(start_date + timedelta(days=7 * i)).strftime("%d %B %Y") for i in range(len(monday_schedule))]
    saturday_dates = [(start_date + timedelta(days=6 + 7 * i)).strftime("%d %B %Y") for i in range(len(saturday_schedule))]

    context = {
        "monday_schedule": zip(monday_dates, [name for name, _ in monday_schedule]),
        "saturday_schedule": zip(saturday_dates, [name for name, _ in saturday_schedule]),
        "prayer_teams": prayer_teams,
        "current_date": datetime.now().strftime("%d %B %Y"),
    }

    return render(request, 'ofele_app/ofele.html', context)
