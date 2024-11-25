# 5. Write a program that inputs an integer and outputs the largest integer 
# that is smaller than or equal to the square root of the input one. [2 points] 

# Input: integer
# Output: integer
import math
def func(num):
    result = 0
    ####### add your code below #######

    result = math.floor(math.sqrt(num))

    ####### add your code above #######
    return result

# test case 1
# Input: 25
# Output: 5
print(func(25))

# test case 2
# Input: 120
# Output: 10
print(func(120))