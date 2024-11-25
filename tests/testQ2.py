import unittest
import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

import Q2 as q2

class Q2TestCase(unittest.TestCase):

  def test_case1(self):
    self.assertEqual(self.q2.func(231), 321)

  def test_case2(self):
    self.assertEqual(self.q2.func(10502), 52100)

  def setUp(self):
    self.q2 = q2

if __name__ == '__main__':
  unittest.main()