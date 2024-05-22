def addition(num1, num2):
    """Return the sum of two numbers."""
    return num1 + num2

def subtraction(num1, num2):
    """Return the difference of two numbers."""
    return num1 - num2

def multiplication(num1, num2):
    """Return the product of two numbers."""
    return num1 * num2

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
    elif operation == '-':
        return subtraction(num1, num2)
    elif operation == '*':
        return multiplication(num1, num2)
    elif operation == '/':
        return division(num1, num2)
    else:
        return "Invalid operation"

# Example usage:
print("Addition Result: ", calculator(10, 5, '+'))  # For addition
print("Subtraction Result: ", calculator(10, 5, '-'))  # For subtraction
print("Multiplication Result: ", calculator(10, 5, '*'))  # For multiplication
print("Division Result: ", calculator(10, 5, '/'))  # For division
