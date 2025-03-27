import pytest
from calc import addition

class Test_SimpleCalculatorAddition:

    @pytest.mark.positive
    def test_addition_of_positive_numbers(self):
        assert addition(3, 5) == 8, "addition of 3 and 5 should be 8"
        
    @pytest.mark.negative
    def test_addition_of_negative_numbers(self):
        assert addition(-3, -5) == -8, "addition of -3 and -5 should be -8"
        
    @pytest.mark.positive
    @pytest.mark.negative
    def test_addition_of_positive_and_negative_numbers(self):
        assert addition(-3, 5) == 2, "addition of -3 and 5 should be 2"
        assert addition(3, -5) == -2, "addition of 3 and -5 should be -2"

    @pytest.mark.float
    def test_addition_of_float_numbers(self):
        assert addition(3.5, 2.1) == 5.6, "addition of 3.5 and 2.1 should be 5.6"

