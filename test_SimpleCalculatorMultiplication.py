import pytest
from calc import multiplication

class Test_SimpleCalculatorMultiplication:

    # Scenario 1: Test with positive integers
    @pytest.mark.regression
    def test_multiplication_positive_integers(self):
        result = multiplication(3, 4)
        assert result == 12, "Multiplication of positive numbers failed"

    # Scenario 2: Test with one zero
    @pytest.mark.regression
    def test_multiplication_zeroes(self):
        result = multiplication(8, 0)
        assert result == 0, "Multiplication with zero failed"

    # Scenario 3: Test with negative numbers
    @pytest.mark.regression
    def test_multiplication_negative_numbers(self):
        result = multiplication(-3, -7)
        assert result == 21, "Multiplication of negative numbers failed"

    # Scenario 4: Test with float numbers
    @pytest.mark.regression
    def test_multiplication_float_numbers(self):
        result = multiplication(3.5, 2.2)
        assert result == 7.7, "Multiplication of float numbers failed"
