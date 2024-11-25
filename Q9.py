# 9. Alex is standing at the ATM to withdraw some cash. ATM will only accept the transaction 
# if the amount Alex is trying to withdraw is a multiple of $5, and his account balance has enough 
# cash for the transaction (including the transaction fee). If there is not enough cash balance 
# in the account to complete the transaction, it does not perform the withdrawal transaction. 
# For each successful withdrawal, there is a transaction fee of $1. Write a program that input 
# two integers (amount Alex wishes to withdraw, initial account balance) and prints out Alex’s 
# account balance after an attempted transaction. [2 points] 
# * Account balance never goes to negative value. 
# * Withdrawal amount of $0 is not considered. 

# Input: integer
# Output: integer

def func(withdraw, balance):
    result = 0
    ####### add your code below #######

    fee = 1
    if (balance < withdraw + fee) or (withdraw == 0) or (withdraw % 5 != 0):
       result = balance
    else:
       result = balance - (withdraw + fee)

    ####### add your code above #######
    return result

# test case 1
# Input: 30, 120
# Output: 89
print(func(30, 120))

# test case 2
# Input: 500, 120
# Output: 120
print(func(500, 120))