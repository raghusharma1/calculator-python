import pytest
from calc import SimpleCalculator

class Test_SimpleCalculatorMultiplication:
    
    @pytest.mark.regression
    @pytest.mark.positive
    def test_multiplication_positive_integers(self):
        # Arrange
        calc = SimpleCalculator()
        num1, num2 = 3, 4
        
        # Act
        result = calc.multiplication(num1, num2)
        
        # Assert
        assert result == 12, 'Multiplication of two positive numbers should return their product'
        
    @pytest.mark.regression
    @pytest.mark.negative
    def test_multiplication_zeroes(self):
        # Arrange
        calc = SimpleCalculator()
        num1, num2 = 8, 0
        
        # Act
        result = calc.multiplication(num1, num2)
        
        # Assert
        assert result == 0, 'Multiplication of any number with zero should return zero'
        
        
    @pytest.mark.regression
    @pytest.mark.positive
    def test_multiplication_negative_numbers(self):
        # Arrange
        calc = SimpleCalculator()
        num1, num2 = -3, -7
        
        # Act
        result = calc.multiplication(num1, num2)
        
        # Assert
        assert result == 21, 'Multiplication of two negative numbers should return a positive number'
        

    @pytest.mark.regression
    @pytest.mark.positive
    def test_multiplication_float_numbers(self):
        # Arrange
        calc = SimpleCalculator()
        num1, num2 = 3.5, 2.2
        
        # Act
        result = calc.multiplication(num1, num2)
        
        # Assert
        assert result == 7.7, 'Multiplication of two floating numbers should return their product'
