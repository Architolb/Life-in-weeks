#  add variables

from tkinter.tix import DisplayStyle


age = input("What is your current age?")
age_as_int = int(age)

years_remaining = 90 - age_as_int


days_remaining = years_remaining * 365

weeks_remaining = years_remaining * 52

months_remaining = years_remaining * 12

# days = 90 - int(age) * 365

# weeks = 90 - int(age) *52

# months = 90 - int(age) * 12


message = f"You currently have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months remaining."
print (message)



