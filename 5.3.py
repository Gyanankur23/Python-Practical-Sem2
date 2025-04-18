import calendar

year = int(input("Enter the year to check: "))
print(calendar.month(year, 3))

print(f"Is the year {year} a leap year? {calendar.isleap(year)}")