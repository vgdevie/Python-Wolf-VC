from datetime import datetime

def get_days_from_today(date):
    try:
        given_date = datetime.strptime(date, '%Y-%m-%d')
        current_date = datetime.today()
        difference = given_date.date() - current_date.date()
        return abs(difference.days)
    except ValueError:
        return "Incorrect date format, should be YYYY-MM-DD"

user_date = input("Enter a date in the format 'YYYY-MM-DD': ")
print(get_days_from_today(user_date))