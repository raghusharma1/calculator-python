import pytest
from calc import subtraction

class Test_SimpleCalculatorSubtraction:
    
    @pytest.mark.regression
    def test_subtraction_valid_positive_integers(self):
        # Arrange
        num1 = 10
        num2 = 5
        expected_result = 5
        
        # Act
        actual_result = subtraction(num1, num2)
        
        # Assert
        assert actual_result == expected_result, 'check subtraction with valid positive integers'
    
    @pytest.mark.regression
    def test_subtraction_with_zero(self):
        # Arrange
        num1 = 0
        num2 = 20

        # Act
        result = subtraction(num1, num2)

        # Assert
        assert result == -num2, 'check subtraction with zero'

        # Check Zero Subtraction
        result = subtraction(num2, num1)
        assert result == num2, 'check zero subtraction'

    @pytest.mark.regression
    def test_subtraction_negative_numbers(self):
        # Arrange
        num1 = -4
        num2 = -3
        expected_result = -1

        # Act
        actual_result = subtraction(num1, num2)

        # Assert
        assert actual_result == expected_result, 'check subtraction with negative numbers'

    @pytest.mark.regression
    def test_subtraction_with_floating(self):
        # Arrange
        num1 = 1.5
        num2 = 0.5
        expected_result = 1.0

        # Act
        actual_result = subtraction(num1, num2)

        # Assert
        assert actual_result == expected_result, 'check subtraction with floating numbers'

    @pytest.mark.regression
    def test_subtraction_same_numbers(self):
        # Arrange
        num = 7

        # Act
        result = subtraction(num, num)

        # Assert
        assert result == 0, 'check subtraction with same numbers'
