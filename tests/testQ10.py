import unittest
import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

import Q10 as q10

class q10TestCase(unittest.TestCase):

  def test_case1(self):
    self.assertEqual(self.q10.func([50, 50, 70, 80, 100]), '40.000%')

  def test_case2(self):
    self.assertEqual(self.q10.func([100, 95, 90, 80, 70, 60, 50]), '57.143%')

  def setUp(self):
    self.q10 = q10

  if __name__ == "__main__":
    unittest.main()