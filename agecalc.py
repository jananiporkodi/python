import time
import datetime
dob = input("enter a date")
a = datetime.datetime.strptime(dob, "%d-%m-%Y").date()
print("DOB = ", a)
today = datetime.date.today()
print("Age = ", end="")
print(today.year - a.year)
