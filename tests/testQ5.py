import unittest
import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

import Q5 as q5

class q5TestCase(unittest.TestCase):

  def test_case1(self):
    self.assertEqual(self.q5.func(25), 5)

  def test_case2(self):
    self.assertEqual(self.q5.func(120), 10)

  def setUp(self):
    self.q5 = q5

  if __name__ == "__main__":
    unittest.main()