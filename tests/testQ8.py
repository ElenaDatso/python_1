import unittest
import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

import Q8 as q8

class q8TestCase(unittest.TestCase):

  def test_case1(self):
    self.assertEqual(self.q8.func(1, 1), 'MON')

  def test_case2(self):
    self.assertEqual(self.q8.func(2, 27), 'TUE')

  def test_case2(self):
    self.assertEqual(self.q8.func(11, 15), 'FRI')

  def setUp(self):
    self.q8 = q8

  if __name__ == "__main__":
    unittest.main()