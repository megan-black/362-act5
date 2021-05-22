# Filename: leap_year.py
# Author: Megan Black
# Description: Program that says if the year entered by the user is a leap year or not.

import unittest
import pytest

class TestCase(unittest.TestCase):
    def test_good(self):
        self.assertEqual(leap(2020), "2020 is a leap year")
        self.assertEqual(leap(1500), "2020 is not a leap year")
        self.assertEqual(leap(1936), "1936 is a leap year")
    def test_bad(self):
        self.assertEqual(leap("abcd"), "Error")
        self.assertEqual(leap(12345), "Error")
        self.assertEqual(leap([2000, 2001]), "Error")

if __name__ == "__main__":
    unittest.main(verbosity=2)
