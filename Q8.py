# 8. January 1st 2024 is Monday. Write a program that input month and date and prints out what day it is.[2 points]
# * 1 <= Month <= 12         1<= Day <= 31 
# * There are 31 days in January, March, May, July, August, October, and December, 30 days in April, June, 
#   September, and November, and 29 days in February, in 2024. 
# * The output should be like this: MON, TUE, WED, THU, FRI, SAT, SUN 

# Input: number
# Output: string
from datetime import datetime as dt

def func(month, date):
    result = 0
    ####### add your code below #######
    year = 2024
    result = dt(year, month, date).strftime("%a").upper()

    ####### add your code above #######
    return result

# test case 1
# Input: 1, 1
# Output: MON
print(func(1,1))

# test case 2
# Input: 2, 27
# Output: TUE
print(func(2, 27))
