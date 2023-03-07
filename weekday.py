import datetime

today = datetime.datetime.today().weekday()
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

if today < 5:
    print("Yes, today is a weekday. It's", weekdays[today])
else:
    print("No, today is a weekend day.")