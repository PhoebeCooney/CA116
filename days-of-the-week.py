#day is a day of the week in the range (1..7).
#1 is Monday, 7 is Sunday.

day = 7 # Sunday

is_college_day = day<=5
is_weekend = not is_college_day
is_ca116_day = day>=2 and day<=4
is_not_ca116_day = not is_ca116_day

print "day is a college day:", is_college_day
print "day is a weekend day:", is_weekend
print "day is ca116 day:", is_ca116_day
print "day is not a ca116 day:", is_not_ca116_day
