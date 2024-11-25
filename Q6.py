# 6. Tim wakes up with an alarm every morning. But he does not always wake up right after 
# he hears his alarm going off and he sometimes is late for work. He decided to 
# set his alarm 35 minutes before the time he needs to wake up. Write a program that 
# outputs the time for Tim to set the alarm according to the input time he needs to wake up. [4 points] 

# * 24-hour system, likes 23:35, 00:01, the output should have 2 digits for hour and 2 digits for minute
# * 0 <= Hour <= 23          0 <= Minute <= 59


# Input: string
# Output: string
import datetime

def func(t):
    result=''
    ####### add your code below #######

    h, m = t.split(":")
    time_to_get_up = datetime.datetime(2024, 1, 1, int(h), int(m))
    time_to_sleep = datetime.timedelta(minutes=35)
    result = (time_to_get_up - time_to_sleep).time().strftime("%H:%M")

    ####### add your code above #######
    return result

# test case 1
# Input: 23:35
# Output: 23:00
print(func('23:35'))

# test case 2
# Input: 09:40
# Output: 09:05
print(func('09:40'))
