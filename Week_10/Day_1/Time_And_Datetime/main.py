from datetime import datetime

current_date = datetime.now()
birthdate = datetime(current_date.year, 10, 26)
count = birthdate - current_date
days_remains = count.days
print(f'My birthday in {count.days} days and {count.seconds} seconds.')