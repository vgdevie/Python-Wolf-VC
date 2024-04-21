from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday_this_year = datetime.strptime(user["birthday"], "%Y.%m.%d").date().replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        days_until_birthday = (birthday_this_year - today).days
        if days_until_birthday <= 7:
            if birthday_this_year.weekday() >= 5:  # if birthday is on weekend
                birthday_this_year += timedelta(days=7 - birthday_this_year.weekday())  # move to next Monday
            upcoming_birthdays.append({'name': user['name'], 'congratulation_date': birthday_this_year.strftime("%Y.%m.%d")})

    return upcoming_birthdays

# Test the function
users = [
    {"name": "John", "birthday": "1990.04.25"},
    {"name": "Alice", "birthday": "1985.12.30"},
    {"name": "Bob", "birthday": "1995.04.23"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print(upcoming_birthdays)
