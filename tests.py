import unittest
from format_price import format_price


class TestPriceFormatting(unittest.TestCase):

    def test_negative_values(self):
        self.assertEqual(format_price('-1234'), '-1 234')
        self.assertEqual(format_price(-1234), '-1 234')
        self.assertEqual(format_price(-1234.00), '-1 234')

    def test_thousands_price(self):
        self.assertEqual(format_price('1234'), '1 234')
        self.assertEqual(format_price(1234), '1 234')
        self.assertEqual(format_price(1234.00), '1 234')

    def test_thousands_with_fractions(self):
        self.assertEqual(format_price('1234.12'), '1 234.12')
        self.assertEqual(format_price(1234.12), '1 234.12')

    def test_thousands_whith_big_fractions(self):
        self.assertEqual(format_price('1234.12334523'), '1 234.12')
        self.assertEqual(format_price('1234.12565665'), '1 234.13')
        self.assertEqual(format_price(1234.12334523), '1 234.12')
        self.assertEqual(format_price(1234.12565665), '1 234.13')

    def test_leading_point(self):
        self.assertEqual(format_price('.01'), '0.01')
        self.assertEqual(format_price(.01), '0.01')

    def test_trailing_point(self):
        self.assertEqual(format_price('150000.'), '150 000')
        self.assertEqual(format_price(150000.), '150 000')

    def test_leading_zeroes(self):
        self.assertEqual(format_price('0001500'), '1 500')

    def test_trailing_zeroes(self):
        self.assertEqual(format_price('1111.1100000'), '1 111.11')
        self.assertEqual(format_price(1111.1100000), '1 111.11')

    def test_wrong_delimiter(self):
        self.assertIsNone(format_price('9999,1231'))
        self.assertIsNone(format_price('3_12'))

    def test_alpabetic_symbols(self):
        self.assertIsNone(format_price('asda'))

    def test_alphanumeric_symbols(self):
        self.assertIsNone(format_price('123ad'))
        self.assertIsNone(format_price('gfsgsg'))

    def test_several_delimiters(self):
        self.assertIsNone(format_price('127.0.0.1'))

    def test_list_input(self):
        self.assertIsNone(format_price([1]))
        self.assertIsNone(format_price([]))

    def test_tuple_input(self):
        self.assertIsNone(format_price((1,2)))

    def test_dict_input(self):
        self.assertIsNone(format_price({'a': 1}))

    def test_none_input(self):
        self.assertIsNone(format_price(None))

    def test_bool_input(self):
        self.assertIsNone(format_price(True))
        self.assertIsNone(format_price(False))

    def test_empty_string(self):
        self.assertIsNone(format_price(''))

    def test_leading_whitespaces(self):
        self.assertEqual(format_price('  3.12'), '3.12')

    def test_trailing_whitespaces(self):
        self.assertEqual(format_price('3.12  '), '3.12')


if __name__ == '__main__':
    unittest.main()
