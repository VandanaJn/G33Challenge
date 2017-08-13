"""Test Class"""
import unittest

from FormatAmount import trunc_decimals, format_ai, format_dp, format_yld

class TestFormatAmount(unittest.TestCase):
    """TestFormatAmount tests FormatAmount module"""
    
    def test_trunc_decimals(self):
        """test_trunc_decimals"""
        self.assertEqual(5.67890, trunc_decimals(5.6789, 5))
        self.assertEqual(5.6789, trunc_decimals(5.6789, 4))
        self.assertEqual(5.6785, trunc_decimals(5.6785, 4))
        self.assertEqual(5.675, trunc_decimals(5.6755, 3))
        self.assertEqual(5.678, trunc_decimals(5.6789, 3))
        self.assertEqual(5.67, trunc_decimals(5.6789, 2))
        self.assertEqual(5.6, trunc_decimals(5.6789, 1))
        self.assertEqual(5, trunc_decimals(5.6789, 0))
        self.assertEqual(5555676.678, trunc_decimals(5555676.6781, 3))

    def test_format_ai(self):
        """test_format_ai"""
        self.assertEqual('5.60', format_ai(5.6))
        self.assertEqual('5.67', format_ai(5.67))
        self.assertEqual('5.68', format_ai(5.6789))
        self.assertEqual('5.68', format_ai(5.6785))
        self.assertEqual('5.67', format_ai(5.6755))## todo seems wrong
        self.assertEqual('5.67', format_ai(5.6749))
        self.assertEqual('5.67', format_ai(5.6744))
        self.assertEqual('5555676.68', format_ai(5555676.6781))

    def test_format_dp(self):
        """test_format_dp"""
        self.assertEqual('5.600', format_dp(5.6))
        self.assertEqual('5.670', format_dp(5.67))
        self.assertEqual('5.678', format_dp(5.6789))
        self.assertEqual('5.678', format_dp(5.6785))
        self.assertEqual('5.675', format_dp(5.6755))
        self.assertEqual('5.674', format_dp(5.6749))
        self.assertEqual('5.674', format_dp(5.6744))
        self.assertEqual('5555676.678', format_dp(5555676.6781))

    def test_format_yld(self):
        """test_format_yld"""
        self.assertEqual(5.600, format_yld(5.6))
        self.assertEqual(5.670, format_yld(5.67))
        self.assertEqual(5.679, format_yld(5.6789))
        self.assertEqual(5.679, format_yld(5.67894))
        self.assertEqual(5.678, format_yld(5.6785))## todo seems wrong
        self.assertEqual(5.676, format_yld(5.6755))## todo investigate
        self.assertEqual(5.675, format_yld(5.6749))
        self.assertEqual(5.674, format_yld(5.6744))
        self.assertEqual(5555676.678, format_yld(5555676.6781))

if __name__ == '__main__':
    unittest.main(exit=False)
