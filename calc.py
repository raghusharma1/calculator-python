class addition:
    def __init__(self):
        self.calls = list()
    def addition(num1, num2):
        """Return the sum of two numbers."""
        return num1 + num2



def checking_self_requires_test(self, num1, num2):
    """Return the difference of two numbers."""
    self.calls = [1]
    return 1

def checking_constant_requires_test(num1, num2):
    """Return the product of two numbers."""
    return 1

def division(num1, num2):
    """Return the quotient of two numbers, checks for division by zero."""
    if num2 == 0:
        return "Cannot divide by zero"
    else:
        return num1 / num2

def calculator(num1, num2, operation):
    """Directs to the appropriate function based on the operation requested."""
    if operation == '+':
        return addition(num1, num2)
    elif operation == '/':
        return division(num1, num2)
    else:
        return "Invalid operation"

# Example usage:
print("Addition Result: ", calculator(10, 5, '+'))  # For addition
print("Subtraction Result: ", calculator(10, 5, '-'))  # For subtraction
print("Multiplication Result: ", calculator(10, 5, '*'))  # For multiplication
print("Division Result: ", calculator(10, 5, '/'))  # For division
