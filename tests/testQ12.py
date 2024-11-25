import unittest
import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

import Q12 as q12

class q12TestCase(unittest.TestCase):

  def test_case1(self):
    self.assertEqual(self.q12.func('Mississippi'), '?')

  def test_case2(self):
    self.assertEqual(self.q12.func('zZa'), 'Z')

  def setUp(self):
    self.q12 = q12

  if __name__ == "__main__":
    unittest.main()
