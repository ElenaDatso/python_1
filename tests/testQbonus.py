import unittest
import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

import QBonus as q_bonus

class q12TestCase(unittest.TestCase):

  def test_case1(self):

    class1 = [
 {'name':"Bob", 'grade':60},
 {'name':"Boe", 'grade':93},
 {'name':"Vaa", 'grade':80},
 {'name':"Vre", 'grade':65},
 {'name':"Toe", 'grade':70},
 ]
    class2 = [{'name':"Dan", 'grade':64},
 {'name':"Don", 'grade':63},
 {'name':"Tim", 'grade':78},
 {'name':"Tom", 'grade':61},
 {'name':"Sebastian Jr.", 'grade':74}
 ]

    self.assertEqual(self.q_bonus.func(class1, class2), ['Boe', 'Tim'])

  def test_case2(self):
    class1 =[ 
 {'name':"Bob", 'grade':60},
 {'name':"Boe", 'grade':50},
 {'name':"Vaa", 'grade':69},
 {'name':"Vre", 'grade':65},
 {'name':"Toe", 'grade':70},
]
    class2 = [
 {'name':"Dan", 'grade':64},
 {'name':"Don", 'grade':63},
 {'name':"Tim", 'grade':71},
 {'name':"Tom", 'grade':61},
 {'name':"Sebastian Jr.", 'grade':74},
]
    self.assertEqual(self.q_bonus.func(class1, class2), ['No one gets a reward.'])

  def setUp(self):
    self.q_bonus = q_bonus

  if __name__ == "__main__":
    unittest.main()
