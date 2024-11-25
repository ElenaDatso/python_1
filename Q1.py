# 1. Write a program that outputs all the numbers that are multiples of 6 from the list in the same 
# order that they appear in the list; stop outputs after 949 in the sequence. [2 points] 
# * List always contains 949. 
# * 949 DOES need to be printed 

# Input: list
# Output: list

def func(numbers):
    result = []
    ####### add your code below #######
    for number in numbers:
        if number % 6 == 0 or number == 949: 
            result.append(number)
            if number == 949:
                break
    ####### add your code above #######
    return result

# test case 1
# Input: [1, 35, 10, 949, 18, 19]
# Output: [949]
print(func([1, 35, 10, 949, 18, 19]))

# test case 2
# Input: [1, 12, 10, 949, 18, 19]
# Output: [12, 949]
print(func([1, 12, 10, 949, 18, 19]))

# test case 3
# Input: [1, 12, 10, 949, 18, 949, 19]
# Output: [12, 949]
print(func([1, 12, 10, 949, 18, 949, 19]))

