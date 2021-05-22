# Filename: leap_year.py
# Author: Megan Black
# Description: Program that says if the year entered by the user is a leap year or not.

import unittest
import pytest

# Function to get if leap year or not
def leap(year):
  year = int(year)
  if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    return year + " is a leap year"
  elif year % 4 == 0 and year % 100 != 0:
    return str(year) + " is a leap year"
  else:
    return str(year) + " is not a leap year"

class TestCase(unittest.TestCase):
  def test_good1(self):
    self.assertEqual(leap(2020), "2020 is a leap year")
  def test_good2(self): 
    self.assertEqual(leap(1500), "1500 is not a leap year")
  def test_good3(self):
    self.assertEqual(leap(1936), "1936 is a leap year")
  def test_bad1(self):
    self.assertRaises(ValueError, leap, "abcd")
  def test_bad2(self):
    self.assertEqual(leap(12345), "Error")
  def test_bad3(self):
    self.assertRaises(TypeError, leap, [2000, 2001])

if __name__ == "__main__":
    unittest.main(verbosity=2)
