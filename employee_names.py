import sys

d = {}

with open("employees.txt") as f:
   lines = f.readlines()

i = 0
while i < len(lines):
   employee = lines[i].split()

   d[employee[0]] = {
   "id" : employee[0],
   "dob" : employee[1],
   "name" : " ".join(employee[2:]),
   }
   i = i + 1

employee_number = sys.stdin.readlines()
j = 0
while j < len(employee_number):
   if employee_number[j].strip() in d:
      sys.stdout.write(d[employee_number[j].strip()]["name"] + "\n")
   j = j + 1
