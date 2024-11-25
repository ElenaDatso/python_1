# 7. You love driving alone on weekends. You are driving on a highway on one Saturday, 
# maybe a little too fast, then a police officer stops you, and asks you to show your 
# driver’s license. Officer is saying, if your speed was 80 or less, you’re not getting 
# any speeding ticket. If your speed was over 80 but less than or equal to 100, you’re 
# getting a small speeding ticket. If your speed was over 100, then you’re getting a big 
# speeding ticket, unless it is your birthday. On your birthday, you can speed 5 higher 
# in all cases. [ 0 = no ticket, 1 = small ticket, 2 = big ticket ] 

# Write a program that computes the result. [4 points]

# Input: dictionary (speed: number, birthday: boolean)
# Output: number

from math import inf


def func(driver):
    result = 0
    ####### add your code below #######

    bd_extra_speed = 5
    allowed_speed = 80
    too_fast_speed = 100
  
    if driver['birthday']:
        allowed_speed += bd_extra_speed
        too_fast_speed += bd_extra_speed

    if driver['speed'] <= allowed_speed:
        result = 0
    elif driver['speed'] <= too_fast_speed:
        result = 1
    else:
        result = 2

    ####### add your code above #######
    return result

# test case 1
# Input: {'speed':79, 'birthday':False}
# Output: 0
print(func({'speed':79, 'birthday': False}))

# test case 2
# Input: {'speed':80, 'birthday':True}
# Output: 0
print(func({'speed':80, 'birthday':True}))
