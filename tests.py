import unittest
from format_price import format_price


class TestPriceFormatting(unittest.TestCase):

    def test_thousands_price(self):
        self.assertEqual(format_price('1234'), '1 234')

    def test_thousands_with_fractions(self):
        self.assertEqual(format_price('1234.12'), '1 234.12')

    def test_thousands_whith_big_fractions(self):
        self.assertEqual(format_price('1234.12334523'), '1 234.12')

    def test_leading_point(self):
        self.assertEqual(format_price('.01'), '0.01')

    def test_trailing_point(self):
        self.assertEqual(format_price('150000.'), '150 000')

    def test_leading_zeroes(self):
        self.assertEqual(format_price('0001500'), '1 500')

    def test_trailing_zeroes(self):
        self.assertEqual(format_price('1111.1100000'), '1 111.11')

    def test_wrong_delimiter(self):
        self.assertIsNone(format_price('9999,1231'))

    def test_alpabetic_symbols(self):
        self.assertIsNone(format_price('asda'))

    def test_alphanumeric_symbols(self):
        self.assertIsNone(format_price('123ad'))

    def test_several_delimiters(self):
        self.assertIsNone(format_price('127.0.0.1'))
