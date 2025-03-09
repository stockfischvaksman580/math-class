import random

def get_random_math_problem():
    # Generate two random numbers between 1 and 10
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    # Choose a random operator (+, -, *, /)
    op = random.choice(["+", "-", "*", "/"])

    # Return the math problem as a string
    return f"{num1} {op} {num2}"
