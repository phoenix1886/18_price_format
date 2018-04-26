from decimal import Decimal, InvalidOperation, ROUND_DOWN


def format_price(price):
    try:
        decimal_price = Decimal(price).quantize(
            Decimal('.01'),
            rounding=ROUND_DOWN)
        precision = 0 if decimal_price % 1 == 0 else 2
    except InvalidOperation:
        return None
    return '{0:,.{1:}f}'.format(decimal_price, precision).replace(',', ' ')


if __name__ == '__main__':
    print('PRICE FORMATTER')
    print('-'*20)
    while True:
        unformated_price = input('Type price for formatting: ')
        message = (
            format_price(unformated_price)
            if unformated_price else
            "Can't perform formatting. Unrecognised price format."
        )
        print(message)
