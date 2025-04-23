import pytest
from calc import division


class Test_CalcDivision:

    def test_division_of_positive_numbers(self):
        # Arrange : No setup required as numbers are passed as parameters

        # Act : Just to invoke division method
        result = division(10, 5)
        
        # Assert
        assert result == 2, "Testing division of two positive numbers failed"

    def test_division_by_zero(self):
        # Arrange : No setup required as numbers are passed as parameters

        # Act : Just to invoke division method
        result = division(10, 0)
        
        # Assert
        assert result == "Cannot divide by zero", "Testing for division by zero failed"

    def test_division_of_negative_numbers(self):
        # Arrange : No setup required as numbers are passed as parameters

        # Act : Just to invoke division method
        result = division(-10, -5)
        
        # Assert
        assert result == 2, "Testing division of two negative numbers failed"


    def test_division_of_positive_and_negative_number(self):
        # Arrange : No setup required as numbers are passed as parameters

        # Act : Just to invoke division method
        result = division(10, -2)
        
        # Assert
        assert result == -5, "Testing division of one positive and one negative number failed"
