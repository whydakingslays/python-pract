#program to display calender of given month and year 

# import calendar module

import calendar

year = int(input('Display your birth year : '))
month = int(input('Display your birth month : '))


# display the calendar of the given month and year
print(calendar.month(year, month))  