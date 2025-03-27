import pytest
from calc import SimpleCalculator

class Test_SimpleCalculatorAddition:
    """
    Pytest class to test the addition method from the SimpleCalculator class
    """

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_add_positive_numbers(self):
        calculator = SimpleCalculator()
        assert calculator.addition(3, 2) == 5

    @pytest.mark.regression
    @pytest.mark.smoke
    def test_add_with_zero(self):
        calculator = SimpleCalculator()
        assert calculator.addition(0, 4) == 4
        assert calculator.addition(4, 0) == 4
        
    @pytest.mark.regression
    @pytest.mark.negative
    def test_add_negative_numbers(self):
        calculator = SimpleCalculator()
        assert calculator.addition(-2, -5) == -7

    @pytest.mark.regression
    def test_add_floating_point(self):
        calculator = SimpleCalculator()
        assert pytest.approx(calculator.addition(0.3, 0.2), 0.5)

    @pytest.mark.regression
    @pytest.mark.performance
    def test_large_number_addition(self):
        calculator = SimpleCalculator()
        assert calculator.addition(10000000000, 20000000000) == 30000000000
