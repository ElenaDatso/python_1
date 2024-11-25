# 12. Write a program that inputs one string and outputs the alphabet that’s 
# used the most in the word, when an English word (might be mixed with upper 
# and lower cases) is given. Your output alphabet should be in uppercase. 
# If there are more than one alphabet that are used the most in the word, output ? [4 points] 

# Input: string with alphabet
# Output: string
from operator import itemgetter

def func(s):
  result = ''
  ####### add your code below #######

  upper_string = s.upper()
  used_letters = {}

  for letter in upper_string:
    if letter not in used_letters:
      count_letters = 0
      for letter_match in upper_string:
        if letter == letter_match: count_letters += 1
      used_letters[letter] = count_letters

  sorted_by_count = sorted([item for item in used_letters.items()], reverse=True, key=itemgetter(1))

  if sorted_by_count[0][1] == sorted_by_count[1][1]:
    result = '?'
  else:
    result = sorted_by_count[0][0]

  ####### add your code above #######
  return result

# test case 1
# Input: Mississippi
# Output: ?
print(func('Mississippi'))

# test case 2
# Input: zZa
# Output: Z
print(func('zZa'))