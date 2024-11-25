import unittest
import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

import Q1 as q1

class Q1TestCase(unittest.TestCase):

  def test_case1(self):
    self.assertEqual(self.q1.func([1, 35, 10, 949, 18, 19]), [949])
    
  def test_case2(self):
    self.assertEqual(self.q1.func([1, 12, 10, 949, 18, 19]), [12, 949])

  def test_case3(self):
    self.assertEqual(self.q1.func([1, 12, 10, 949, 18, 949, 19]), [12, 949])

  def setUp(self):
    self.q1 = q1

if __name__ == '__main__':
  unittest.main()