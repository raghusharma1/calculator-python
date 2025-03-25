# Import necessary libraries
import pytest
from calc import SimpleCalculator

# Define the test class
class Test_SimpleCalculatorAddition:

    # Scenario 1: Testing addition of two positive numbers
    @pytest.mark.positive
    def test_addition_positive_numbers(self):
        # Arrange
        num1, num2 = 5, 7
        calculator = SimpleCalculator()

        # Act
        result = calculator.addition(num1, num2)

        # Assert
        assert result == 12, "Addition of two positive numbers does not match the expected result"

    # Scenario 2: Testing addition of two negative numbers
    @pytest.mark.negative
    def test_addition_negative_numbers(self):
        # Arrange
        num1, num2 = -3, -5
        calculator = SimpleCalculator()

        # Act
        result = calculator.addition(num1, num2)

        # Assert
        assert result == -8, "Addition of two negative numbers does not match the expected result"
        
    # Scenario 3: Testing addition of a positive and a negative number
    @pytest.mark.mix
    def test_addition_positive_negative_numbers(self):
        # Arrange
        num1, num2 = -3, 5
        calculator = SimpleCalculator()

        # Act
        result = calculator.addition(num1, num2)

        # Assert
        assert result == 2, "Addition of positive and negative numbers does not match the expected result"
        
    # Scenario 4: Testing addition with zero
    @pytest.mark.zero
    def test_addition_with_zero(self):
        # Arrange
        num1, num2 = 7, 0
        calculator = SimpleCalculator()

        # Act
        result = calculator.addition(num1, num2)

        # Assert
        assert result == 7, "Addition of a number with zero does not match the expected result"
