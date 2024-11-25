# [BONUS] Adrienne teaches two grade 12 Math classes. After every test, 
# Adrienne likes to enter her students names and grades as key:value pairs 
# in a list (e.g. [{‘Bob’: 91}, {‘Moe’: 52}, {‘Ben’: 82}, {‘John’: 70}, {`Tim’: 62}]) 
# and gives the highest scoring student in each class a reward (as long as their grade is >75). 
# She has a separate list for each of her classes. Write a program that returns 
# the name of the highest scoring student in each class in a list. 
# If more than one student got the highest grade (e.g. [{‘Bob’: 91}, {‘Moe’: 91}]) 
# Adrienne rewards all of them for their achievement. [4 points] 

# * If there is no student from any of the classes that qualifies for the reward, 
#   it should output “No one gets a reward.” 
# * Every student has a unique name (no duplicate) 

# Input: dictionary
# Output: list

def func(score1, score2):
  result = []
  ####### add your code below #######

  def best_student_from(list):
    best_score = 75
    best_stud = ''

    for item in list:
      for key in item:
        if key == 'grade' and item[key] > best_score:
          best_score = item[key]
          best_stud = item['name']
    if best_stud: result.append(best_stud)

  best_student_from(score1)
  best_student_from(score2)

  if bool(result) == False: result.append("No one gets a reward.")

  ####### add your code above #######
  return result

# test case 1
# Input: [ 
#  {'name':"Bob", 'grade':60},
#  {'name':"Boe", 'grade':93},
#  {'name':"Vaa", 'grade':80},
#  {'name':"Vre", 'grade':65},
#  {'name':"Toe", 'grade':70},
# ],
# [
#  {'name':"Dan", 'grade':64},
#  {'name':"Don", 'grade':63},
#  {'name':"Tim", 'grade':78},
#  {'name':"Tom", 'grade':61},
#  {'name':"Sebastian Jr.", 'grade':74},
# ]

# Output: ['Boe', 'Tim']

print(func([ 
 {'name':"Bob", 'grade':60},
 {'name':"Boe", 'grade':93},
 {'name':"Vaa", 'grade':80},
 {'name':"Vre", 'grade':65},
 {'name':"Toe", 'grade':70},
],
[
 {'name':"Dan", 'grade':64},
 {'name':"Don", 'grade':63},
 {'name':"Tim", 'grade':78},
 {'name':"Tom", 'grade':61},
 {'name':"Sebastian Jr.", 'grade':74},
]))

# test case 2
# Input: [ 
#  {'name':"Bob", 'grade':60},
#  {'name':"Boe", 'grade':50},
#  {'name':"Vaa", 'grade':69},
#  {'name':"Vre", 'grade':65},
#  {'name':"Toe", 'grade':70},
# ],
# [
#  {'name':"Dan", 'grade':64},
#  {'name':"Don", 'grade':63},
#  {'name':"Tim", 'grade':71},
#  {'name':"Tom", 'grade':61},
#  {'name':"Sebastian Jr.", 'grade':74},
# ]

# Output: ['No one gets a reward.']

print(func([ 
 {'name':"Bob", 'grade':60},
 {'name':"Boe", 'grade':50},
 {'name':"Vaa", 'grade':69},
 {'name':"Vre", 'grade':65},
 {'name':"Toe", 'grade':70},
],
[
 {'name':"Dan", 'grade':64},
 {'name':"Don", 'grade':63},
 {'name':"Tim", 'grade':71},
 {'name':"Tom", 'grade':61},
 {'name':"Sebastian Jr.", 'grade':74},
]))





