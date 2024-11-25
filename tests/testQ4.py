import unittest
import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

import Q4 as q4

class Q4TestCase(unittest.TestCase):

  def test_case1(self):
    self.assertEqual(self.q4.func(55, -81, 39), -81)

  def test_case2(self):
    self.assertEqual(self.q4.func(5, 5.5, 0), 5.5)

  def setUp(self):
    self.q4 = q4

  if __name__ == "__main__":
    unittest.main()