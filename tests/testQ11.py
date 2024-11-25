import unittest
import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

import Q11 as q11

class q11TestCase(unittest.TestCase):

  def test_case1(self):
    self.assertEqual(self.q11.func([3,3,3]), 130)

  def test_case2(self):
    self.assertEqual(self.q11.func([1,3,5]), 5)

  def test_case3(self):
    self.assertEqual(self.q11.func([1,2,1]), 11)

  def setUp(self):
    self.q11 = q11

  if __name__ == "__main__":
    unittest.main()