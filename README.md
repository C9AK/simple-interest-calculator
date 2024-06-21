# Simple Interest Calculator

This repository contains a Python script to calculate simple interest. This is part of a micro-finance startup's mission to empower low-income individuals by providing financial tools.

## Usage

To calculate simple interest, you can use the `calculate_simple_interest` function in `simple_interest.py`.

```python
def calculate_simple_interest(principal, rate, time):
    # principal: The principal amount
    # rate: The rate of interest per year
    # time: The time the money is invested for in years
    # return: The simple interest
    ```

## Example

```python
principal = 1000  # in dollars
rate = 5  # annual interest rate in percent
time = 2  # in years

interest = calculate_simple_interest(principal, rate, time)
print(f"The simple interest is: ${interest}")
