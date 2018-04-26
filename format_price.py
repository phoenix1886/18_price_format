from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('price', help='unformatted price', type=Decimal)
    return parser.parse_args()


def check_input_data_type(input_data):
    if isinstance(input_data, bool):
        return False
    if isinstance(input_data, (int, Decimal, str)):
        return True
    return False


def format_price(price, check_data_types_function=check_input_data_type):
    if not check_data_types_function(price):
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
