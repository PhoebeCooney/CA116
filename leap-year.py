year = 2008

is_a_leap_year = (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)) 

print year, "is a leap year:", is_a_leap_year
