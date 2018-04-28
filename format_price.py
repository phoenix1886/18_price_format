from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
import argparse
import re


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('price', help='unformatted price')
    return parser.parse_args()


def format_price(price):
    if not isinstance(price, str):
        return None
    price = price.strip()
    if not re.fullmatch(r'\d*\.*\d*', price):
        return None

    try:
        decimal_price = Decimal(price).quantize(
            Decimal('.01'),
            rounding=ROUND_HALF_UP
        )
        precision = 0 if decimal_price % 1 == 0 else 2
    except InvalidOperation:
        return None
    return '{0:,.{1:}f}'.format(decimal_price, precision).replace(',', ' ')


if __name__ == '__main__':
    arguments = parse_arguments()
    print(format_price(arguments.price))
