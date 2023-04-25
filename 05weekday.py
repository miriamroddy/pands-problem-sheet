
## Write a program that outputs whether or not today is a weekday. The program should be called weekday.py.
## You will need to search the web to find how you work out what day it is.

## We start by importing the datetime module, which allows us to manipulate date and time object data.

import datetime

## We use the module to get the day of the week for the current date and time - this is then stored in the today variable. We do this by calling the weekday() 
## method of the today object, which returns an integer representing the day of the week, with Monday being a 0 and Sunday being a 6.

today = datetime.datetime.today().weekday()

## We then create a list called weekdays, with each string in the list representing a weekday - Monday is 0 and Friday is 4.

weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")

## We now use an if statement to check if the day of the week is less than 5. If the day of the week is less than 5, we know that it must be a weekday (because Monday's index is 0 and Thursday's is 4),
## so we output the "Yes, today is a weekday" message to the console. If the day of the week is 5 or 6, it must be a weekend 
## (Saturday or Sunday), so we output the message "No, today is not a weekday."

if today < 5:
    print("Yes, today is a weekday. It's", weekdays[today])
else:
    print("No, today is a weekend day.")
