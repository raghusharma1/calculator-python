import pytest
import random
from calc import division

class Test_CalcDivision:

    @pytest.mark.regression
    @pytest.mark.positive
    def test_regular_division(self):
        num1, num2 = random.randint(1, 100), random.randint(1, 100)
        result = division(num1, num2)
        assert result == num1 / num2, f"Expected {num1/num2} but got {result}"

    @pytest.mark.regression
    @pytest.mark.negative
    def test_division_by_zero(self):
        num1, num2 = random.randint(1, 100), 0
        result = division(num1, num2)
        assert result == "Cannot divide by zero", f"Expected 'Cannot divide by zero' but got {result}"

    @pytest.mark.regression
    @pytest.mark.negative
    def test_negative_division(self):
        num1, num2 = random.randint(-100, -1), random.randint(-100, -1)
        result = division(num1, num2)
        assert result == num1 / num2, f"Expected {num1/num2} but got {result}"

    @pytest.mark.regression
    @pytest.mark.positive
    def test_fractional_division(self):
        num1, num2 = random.uniform(0.1, 10.0), random.uniform(0.1, 10.0)
        result = division(num1, num2)
        assert pytest.approx(result) == num1 / num2, f"Expected {num1/num2} but got {result}"
