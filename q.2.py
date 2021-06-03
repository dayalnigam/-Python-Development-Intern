#2: Write a Python program to calculate the number of days between two dates.Sample dates : (20200702), (20200711)
from datetime import date
a=date(2020,7,2)
b=date(2020,7,11)
c=b-a
print(c)