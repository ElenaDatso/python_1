import unittest
import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

import Q9 as q9

class q9TestCase(unittest.TestCase):

  def test_case1(self):
    self.assertEqual(self.q9.func(30, 120), 89)

  def test_case2(self):
    self.assertEqual(self.q9.func(500, 120), 120)

  def test_case3(self):
    self.assertEqual(self.q9.func(112, 120), 120)

  def test_case4(self):
    self.assertEqual(self.q9.func(112, 0), 0)

  def test_case4(self):
    self.assertEqual(self.q9.func(0, 112), 112)

  def test_case4(self):
    self.assertEqual(self.q9.func(110, 110), 110)

  def setUp(self):
    self.q9 = q9

  if __name__ == "__main__":
    unittest.main()