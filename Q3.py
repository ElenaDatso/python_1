# 3. Write a program to calculate the perimeter of the triangle, 
# based on the three points given by user. [2 points]

# Input: tuple
# Output: number
import math

def func(a,b,c):
    result = 0
    ####### add your code below #######

    x1, y1 = a
    x2, y2 = b
    x3, y3 = c

    #The distance from point P(x1,y1) to point Q(x2,y2) is:
    # Distance = √ ( (x2 - x1)2 + (y2 - y1)2 )
    # source: https://www.wyzant.com/resources/answers/746647/find-the-perimeter-of-the-triangle-with-vertices-a-5-2-b-2-2-and-c-5-2

    def side_length(pointA_x, pointB_x, pointA_y, pointB_y):
      return math.sqrt((pointA_x - pointB_x) ** 2 + (pointA_y - pointB_y) ** 2)

    ab = side_length(x2, x1, y2, y1)
    ac = side_length(x3, x1, y3, y1)
    bc = side_length(x3, x2, y3, y2)

    result = int(ab + bc + ac)
    ####### add your code above #######
    return result

# test case 1
# Input: (5, 1), (5, 4), (1, 1)
# Output: 12
print(func((5, 1), (5, 4), (1, 1)))

# test case 2
# Input: (0, 0), (3, 0), (0, 4)
# Output: 12
print(func((0, 0), (3, 0), (0, 4)))
