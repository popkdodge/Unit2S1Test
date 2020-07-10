#!/usr/bin/env python

import unittest
from lambdastu import Lambdastudents, DataSci

user1 = DataSci('Cook', 'Rob', 34, 16)
user2 = DataSci('Student', 'Noah', 26, 16)
class TestLambdastudents(unittest.TestCase):

  def testcode(self):

      self.assertEqual(user1.age, 34)
      self.assertEqual(user2.age, 26)
      return "All test pass successfuly."



if __name__ =='__main__':
    unittest.main()