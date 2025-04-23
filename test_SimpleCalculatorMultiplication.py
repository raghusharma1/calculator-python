import pytest
from calc import multiplication

class Test_SimpleCalculatorMultiplication:

    def test_positive_integer_multiplication(self):
        assert multiplication(5, 10) == 50, "Test Failed: 5 and 10 should yield 50"
    
    def test_zero_operand_multiplication(self):
        assert multiplication(10, 0) == 0, "Test Failed: Any number multiplied by 0 should yield 0"
    
    def test_negative_integer_multiplication(self):
        assert multiplication(-2, -3) == 6, "Test Failed: -2 and -3 should yield 6"
    
    def test_mixed_sign_multiplication(self):
        assert multiplication(-2, 3) == -6, "Test Failed: -2 and 3 should yield -6"
      
    def test_decimal_number_multiplication(self):
        assert multiplication(0.5, 0.2) == 0.1, "Test Failed: 0.5 and 0.2 should yield 0.1"
