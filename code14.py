#Check if a year is a leap year

def leap_year(n):
    if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
        return True
    else:
        return False

year = 2020

if leap_year(year):
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")