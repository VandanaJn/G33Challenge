"""Test Class"""
import unittest

from Program import format_amt, amt_prompt

class TestProgram(unittest.TestCase):
    """TestProgram - Tests functions of Program"""
    def test_format_amt(self):
        """format_amt - formats based on type, A, D Y"""
        self.assertEqual('ACCRUED INTEREST: 5.67', format_amt('A', 5.6666))
        self.assertEqual('DOLLAR PRICE: 5.666', format_amt('D', 5.6666))
        self.assertEqual('YIELD: 5.667', format_amt('Y', 5.6666))

    def test_amt_prompt(self):
        """format_amt - formats based on type, A, D Y"""
        self.assertEqual('ENTER ACCRUED INTEREST: ', amt_prompt('A'))
        self.assertEqual('ENTER DOLLAR PRICE: ', amt_prompt('D'))
        self.assertEqual('ENTER YIELD: ', amt_prompt('Y'))
        self.assertEqual('ENTER NUMBER: ', amt_prompt('N'))

if __name__ == '__main__':
    unittest.main(exit=False)
