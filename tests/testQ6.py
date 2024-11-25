import unittest
import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

import Q6 as q6

class q6TestCase(unittest.TestCase):

  def test_case1(self):
    self.assertEqual(self.q6.func('23:35'), '23:00')

  def test_case2(self):
    self.assertEqual(self.q6.func('09:40'), '09:05')

  def test_case3(self):
    self.assertEqual(self.q6.func('12:15'), '11:40')

  def setUp(self):
    self.q6 = q6

  if __name__ == "__main__":
    unittest.main()