import unittest
import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

import Q7 as q7

class q7TestCase(unittest.TestCase):

  def test_case1(self):
    self.assertEqual(self.q7.func({'speed':79, 'birthday': False}), 0)

  def test_case2(self):
    self.assertEqual(self.q7.func({'speed':80, 'birthday':True}), 0)

  def test_case3(self):
    self.assertEqual(self.q7.func({'speed':86, 'birthday':True}), 1)

  def test_case3(self):
    self.assertEqual(self.q7.func({'speed':101, 'birthday':True}), 1)

  def test_case3(self):
    self.assertEqual(self.q7.func({'speed':101, 'birthday':False}), 2)

  def setUp(self):
    self.q7 = q7

  if __name__ == "__main__":
    unittest.main()