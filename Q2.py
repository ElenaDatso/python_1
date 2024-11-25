# 2. Write a program that sorts a given number’s digits in descending order and prints it. [2 points]
# *The number is always a positive integer. 

# Input: number
# Output: number

def func(num):
    result = 0
    ####### add your code below #######

    result = int("".join(sorted(str(num), reverse=True)))

    ####### add your code above #######
    return result

# test case 1
# Input: 231
# Output: 321
print(func(231))

# test case 2
# Input: 10502
# Output: 52100
print(func(10502))

