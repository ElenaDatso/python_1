import unittest
import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

import Q3 as q3

class Q3TestCase(unittest.TestCase):

  def test_case1(self):
    self.assertEqual(self.q3.func((5, 1), (5, 4), (1, 1)), 12)

  def test_case2(self):
    self.assertEqual(self.q3.func((0, 0), (3, 0), (0, 4)), 12)

  def setUp(self):
    self.q3 = q3
  
  if __name__ == "__main__":
    unittest.main()