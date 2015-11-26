import time
import datetime
dob = input("enter a date (DD-MM-YYYY)")
try:
	a = datetime.datetime.strptime(dob, "%d-%m-%Y").date()
	print("DOB = ", a)
	today = datetime.date.today()
	print("Age = ", end="")
	print(today.year - a.year)
except:
	print("Please enter a valid date and in the specified format")
