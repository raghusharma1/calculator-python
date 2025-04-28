# First, import the necessary libraries and modules.
import pytest
from calc import SimpleCalculator

# Define the class Test_SimpleCalculatorAddition for pytest to recognise these as unit tests.
class Test_SimpleCalculatorAddition:

    # Define the tests according to the given scenarios.
    
    # Test Scenario 1: Add Two Positive Numbers
    def test_add_positive_numbers(self):
        # Test Setup (Arrange)
        calculator = SimpleCalculator()

        # Invoke the method with two positive integers (Act)
        result = calculator.addition(5, 7)

        # Check if the result is as expected (Assert)
        assert result == 12, "Addition of two positive numbers failed"

    # Test Scenario 2: Addition with Zero
    def test_add_with_zero(self):
        # Test Setup (Arrange)
        calculator = SimpleCalculator()

        # Invoke the method with one number as zero (Act)
        result = calculator.addition(0, 7)

        # Check if the result is as expected (Assert)
        assert result == 7, "Addition with zero failed"
    
    # Test Scenario 3: Addition of Negative Numbers
    def test_add_negative_numbers(self):
        # Test Setup (Arrange)
        calculator = SimpleCalculator()

        # Invoke the method with two negative integers(Act)
        result = calculator.addition(-3, -2)

        # Check if the result is as expected (Assert)
        assert result == -5, "Addition of two negative numbers failed"
    
    # Test Scenario 4: Addition of Floating Points
    def test_add_floating_point(self):
        # Test Setup (Arrange)
        calculator = SimpleCalculator()

        # Invoke the method with two floating point numbers(Act)
        result = calculator.addition(1.5, 2.7)

        # Check if the result is as expected (Assert)
        assert result == 4.2, "Addition of floating point numbers failed"

    # Test Scenario 5: Addition with Large Numbers
    def test_large_number_addition(self):
        # Test Setup (Arrange)
        calculator = SimpleCalculator()

        # Invoke the method with two very large numbers(Act)
        result = calculator.addition(10**10, 10**10)

        # Check if the result is as expected (Assert)
        assert result == 2 * 10**10, "Addition of very large numbers failed"
