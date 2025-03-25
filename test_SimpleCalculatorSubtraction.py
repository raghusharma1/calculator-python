import pytest
from calc import subtraction

class Test_SimpleCalculatorSubtraction:
  
    # Test scenario 1: Validate subtraction operation of two positive integers
    def test_subtraction_of_positive_integers(self):
        num1 = 7
        num2 = 2
        result = subtraction(num1,num2)
        assert result == 5, "The subtraction of 7 and 2 should be 5"

    # Test scenario 2: Zero subtraction operation
    def test_zero_subtraction(self):
        num1 = 0
        num2 = 5
        result = subtraction(num1,num2)
        assert result == -5, "Subtracting 5 from 0 should return -5"

    # Test scenario 3: Subtracting negative integers
    def test_subtraction_of_negative_integers(self):
        num1 = -3
        num2 = -7
        result = subtraction(num1,num2)
        assert result == 4, "Subtracting -7 from -3 should return 4"

    # Test scenario 4: Subtracting floating point numbers
    def test_subtraction_of_floats(self):
        num1 = 9.2
        num2 = 4.5
        result = subtraction(num1,num2)
        assert pytest.approx(result) == 4.7,"The subtraction of 9.2 and 4.5 should be 4.7"
