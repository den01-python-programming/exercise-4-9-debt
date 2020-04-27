# Exercise 4.9 Debt

Create the class `Debt` that has double-typed instance variables of `balance` and `interest_rate`. The balance and the interest rate are passed to the constructor as parameters `def __init__(self, initial_balance, initial_interest_rate)`.

In addition, create the methods `def print_balance()` and `def wait_one_year()` for the class. The method print_balance prints the current balance, and the wait_one_year method grows the debt amount.

The debt is increased by multiplying the balance by the interest rate.

The class should do the following:

```python
def main():

    mortgage = Debt(120000.0, 1.01)
    mortgage.print_balance()

    mortgage.wait_one_year()
    mortgage.print_balance()

    years = 0

    while (years < 20):
        mortgage.wait_one_year()
        years = years + 1

    mortgage.print_balance()
```

The example above illustrates the development of a mortgage with an interest rate of one percent.

Prints:

```plaintext
120000.0
121200.0
147887.0328416936
```

When you've managed to get the program to work, check the previous example with the early 1900s recession interest rates as well.

Once you get the program to work, try out the previous example with the interest rates of the early 1990s recession when the interest rates were as high as 15-20% - try swapping the interest rate in the example above with `1.20` and see what happens.
