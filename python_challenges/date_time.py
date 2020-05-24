import datetime

time=datetime.datetime.now()
month=str(time.month)
day=str(time.day)
hour=str(time.hour)
minute=str(time.minute)

print(f'current date and time: {month}/{day}   and    {hour}:{minute} ')