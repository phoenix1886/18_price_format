# Price Formatter

This script is designed for formatting prices.
It groups thousand parts and separates them by
spaces as in the following example:
`100000 -> 100 000`.
It also limits the precision of prices by 2, rounding
prices `10.025 -> 10.03`.

If price has no fraction part, no fraction part
is returned.

To run the script, one should have python 3.5 installed,
no side packages required.

To run the script one should run `format_price.py` with one positional
argument `price` (numeric value), i.e. `python format_price.py <price>`.

## Example of script work on Linux
```bash
$ python format_price.py 1500.125
1 500.13
$ python format_price.py 1500.124
1 500.12
```

## How to import price_format function
```python
from format_price import format_price
```
Imported `format_price` function can work with string input, as well as
with integers and decimal, otherwise it returns None. It doesn't accept
float prices, because of unpredicted rounding results.

## Example of format_price function work
```python
>>> format_price(Decimal('.015'))
'0.02'
>>> format_price('1000.025')
'1 000.03'
>>> format_price(1000)
'1 000'
```

## How to run test
```bash
python tests.py
................
----------------------------------------------------------------------
Ran 16 tests in 0.003s

OK
```


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
