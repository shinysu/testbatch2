"""
factorial.py - finds the factorial of a number using recursion
"""

def get_factorial(number):
    if number == 0:
        return 1
    else:
        return number * get_factorial(number-1)


factorial = get_factorial(6)
print(factorial)