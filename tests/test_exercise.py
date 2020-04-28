import pytest
from src.debt import Debt

def test_exercise(capsys):
    mortgage = Debt(120000.0, 1.01)
    mortgage.print_balance()

    mortgage.wait_one_year()
    mortgage.print_balance()

    years = 0

    while (years < 20):
        mortgage.wait_one_year()
        years = years + 1

    mortgage.print_balance()

    out, err = capsys.readouterr()
    assert out == "120000.0\n121200.0\n147887.0328416936\n"
