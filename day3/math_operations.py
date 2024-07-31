import numpy as np

def add(a, b):
    """
    adds a together with b

    a : the first addend in the addition
    b : the second addend in the addition
    """

    return a + b


def subtract(a, b):
    """
    subtracts a from b

    a : the minuend in the subtraction
    b : the subtrahend in the subtraction
    """

    return a - b


def multiply(a, b):
    """
    multiplies a togther with b

    a : the first multiplicand in the multiplication
    b : the second multiplicand in the multiplication
    """

    return a * b


def divide(a, b):
    """
    Divides a by b

    a : the dividend in the division
    b : the divisor in the division
    """

    return a / b


def mean(numbers):
    """
    calculates the mean of numbers

    numbers : numpy array of numbers
    """

    return np.mean(numbers)

print(mean(np.array([1,2,4,5,6,78,8,9])))
