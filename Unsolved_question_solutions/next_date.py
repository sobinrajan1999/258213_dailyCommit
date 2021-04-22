# Python program to display next date
leap_year = False
month = 0
year = int(input("Enter year: "))
if year % 400 == 0:
    leap_year = True
elif year % 100 == 0:
    leap_year = False
elif year % 4 == 0:
    leap_year = True
else:
    leap_year = True

month = int(input('Enter month: '))
if month in [1, 3, 5, 7, 8, 10, 12]:
    month_days = 31
elif month == 2 and leap_year == True:
    month_days = 29
elif month == 2 and leap_year == False:
    month_days = 28
else:
    month_days = 30

day = int(input("Enter day: "))

if day < month_days:
    day += 1
else:
    day = 1
if month == 12:
    month = 1
    year+=1

print("Next day is: {}-{}-{}".format(day, month, year))
