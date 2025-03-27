import pytest
from calc import SimpleCalculator

class Test_SimpleCalculatorMultiplication:
    
    # Scenario 1: Test with positive integers
    @pytest.mark.regression
    def test_multiplication_positive_integers(self):
        calculator = SimpleCalculator()
        assert calculator.multiplication(3, 4) == 12
        
    # Scenario 2: Test with one zero
    @pytest.mark.regression
    def test_multiplication_zeroes(self):
        calculator = SimpleCalculator()
        assert calculator.multiplication(8, 0) == 0 

    # Scenario 3: Test with negative numbers
    @pytest.mark.regression
    def test_multiplication_negative_numbers(self):
        calculator = SimpleCalculator()
        assert calculator.multiplication(-3, -7) == 21 
        
    # Scenario 4: Test with float numbers
    @pytest.mark.regression
    def test_multiplication_float_numbers(self):
        calculator = SimpleCalculator()
        assert calculator.multiplication(3.5, 2.2) == 7.7  
