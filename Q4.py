# 4. Write a program that outputs the number that has 
# the largest absolute value among the three numbers. [2 points]

# Input: number
# Output: number

def func(num1, num2, num3):
    result = 0
    ####### add your code below #######

    def to_abs(e):
      return abs(e)
    result = sorted([num1, num2, num3], key = to_abs)[-1]

    ####### add your code above #######
    return result

# test case 1
# Input: 55, -81, 39
# Output: -81
print(func(55, -81, 39))

# test case 2
# Input: 5, 5.5, 0
# Output: 5.5
print(func(5, 5.5, 0))