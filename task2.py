
from datetime import datetime


x = int(input("enter year: "))
def get_century(year):
    if (year % 100 == 0):
        print(year // 100)
    else : 
        print(year // 100 + 1)
get_century(x)        