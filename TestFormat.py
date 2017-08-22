"""Test Class"""
import unittest
import math

from FormatAmount import trunc_decimals, format_ai, format_dp, format_yld, g33_round

class TestFormatAmount(unittest.TestCase):
    """TestFormatAmount tests FormatAmount module"""
    def test_trunc_decimals(self):
        """test_trunc_decimals - returns trucates val to no_of_digits after decimal"""
        self.assertEqual(5.67890, trunc_decimals(5.6789, 5))
        self.assertEqual(5.6789, trunc_decimals(5.6789, 4))
        self.assertEqual(5.6785, trunc_decimals(5.6785, 4))
        self.assertEqual(5.675, trunc_decimals(5.6755, 3))
        self.assertEqual(5.675, trunc_decimals(5.6756, 3))
        self.assertEqual(5.678, trunc_decimals(5.6789, 3))
        self.assertEqual(5.67, trunc_decimals(5.6789, 2))
        self.assertEqual(5.6, trunc_decimals(5.6789, 1))
        self.assertEqual(5, trunc_decimals(5.6789, 0))
        self.assertEqual(5555676.678, trunc_decimals(5555676.6781, 3))

    def test_format_ai(self):
        """test_format_ai - returns truncated to three decimal places,
        and rounded to two decimal place"""
        self.assertEqual(5.60, format_ai(5.6))
        self.assertEqual(5.67, format_ai(5.67))
        self.assertEqual(5.68, format_ai(5.6789))
        self.assertEqual(5.68, format_ai(5.6785))
        self.assertEqual(5.68, format_ai(5.6755))
        self.assertEqual(5.67, format_ai(5.6749))
        self.assertEqual(5.67, format_ai(5.6744))
        self.assertEqual(5555676.68, format_ai(5555676.6781))

    def test_format_dp(self):
        """test_format_dp -  returns truncated to three decimal places"""
        self.assertEqual(5.600, format_dp(5.6))
        self.assertEqual(5.670, format_dp(5.67))
        self.assertEqual(5.678, format_dp(5.6789))
        self.assertEqual(5.678, format_dp(5.6785))
        self.assertEqual(5.675, format_dp(5.6755))
        self.assertEqual(5.674, format_dp(5.6749))
        self.assertEqual(5.674, format_dp(5.6744))
        self.assertEqual(5555676.678, format_dp(5555676.6781))

    def test_format_yld(self):
        """test_format_yld returns truncated to four decimal places,
        and rounded to three decimal places"""
        self.assertEqual(5.600, format_yld(5.6))
        self.assertEqual(5.670, format_yld(5.67))
        self.assertEqual(5.679, format_yld(5.6789))
        self.assertEqual(5.679, format_yld(5.67894))
        self.assertEqual(5.679, format_yld(5.6785))
        self.assertEqual(5.676, format_yld(5.6755))
        self.assertEqual(5.675, format_yld(5.6749))
        self.assertEqual(5.674, format_yld(5.6744))
        self.assertEqual(5555676.678, format_yld(5555676.6781))

    def test_g33_round(self):
        """test_g33_round - returns rounded no to no_of_digits decimal places,
        g33_round(4.65 , 1) returns 4.7 and g33_round(4.55 , 1) returns 4.6"""
        self.assertEqual(5.6, g33_round(5.6, 1))
        self.assertEqual(5.6, g33_round(5.64, 1))
        self.assertEqual(5.7, g33_round(5.65, 1))
        self.assertEqual(5.7, g33_round(5.66, 1))
        self.assertEqual(5.65, g33_round(5.65, 2))
        self.assertEqual(5.65, g33_round(5.651, 2))
        self.assertEqual(5.65, g33_round(5.654, 2))
        self.assertEqual(5.66, g33_round(5.655, 2))
        self.assertEqual(5.68, g33_round(5.675, 2))
        self.assertEqual(4.7, g33_round(4.65, 1))
        self.assertEqual(4.6, g33_round(4.55, 1))

    def test_g33_round_negative(self):
        """test_g33_round_negative - returns rounded no to no_of_digits decimal places,
        test cases for negatives"""
        self.assertEqual(-23.57, g33_round(-23.567, 2))
        self.assertEqual(-23.57, g33_round(-23.566, 2))
        self.assertEqual(-23.56, g33_round(-23.565, 2))
        self.assertEqual(-23.56, g33_round(-23.564, 2))
        self.assertEqual(-23.56, g33_round(-23.557, 2))
        self.assertEqual(-23.56, g33_round(-23.556, 2))
        self.assertEqual(-23.55, g33_round(-23.555, 2))
        self.assertEqual(-23.55, g33_round(-23.554, 2))

    def test_ceil(self):
        """test_ceil tests math.ceil, which is used in g33_round"""
        self.assertEqual(-2356, math.ceil(-2356.5))
        self.assertEqual(2357, math.ceil(2356.5))
        self.assertEqual(6, math.ceil(5.5))

if __name__ == '__main__':
    unittest.main(exit=False)
