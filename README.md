# Price Formatter

This script is designed for formatting prices.
It groups thousand parts and separates them by
spaces as in the following example:
`100000 -> 100 000`.
It also limits the precision of prices by 2, rounding
prices down `10.025 -> 10.02`.

If price has no fraction part, no fraction part
is returned.

To run the script, one should have python 3.5 installed,
no side packages required.

## How to run in bash (Linux)
```bash
python format_price.py
Type price for formatting: 1000.015
1 000.01
Type price for formatting: .95
0.95
Type price for formatting: ..ads
None
```
Script works in infinite loop, waiting for user's input.
To interrupt the script, press **ctrl+C**.

## How to import price_format_function
```python
from format_price import format_price
```



# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
