import random

def get_random_math_problem():
    # Generate a random number between 1 and 10
    num1 = random.randint(1, 10)
    # Generate another random number between 1 and 10
    num2 = random.randint(1, 10)
    # Generate a random operation (+, -, *, /)
    op = random.choice(['+', '-', '*', '/'])
    if op == '+':
        return f"{num1} + {num2}"
    elif op == '-':
        return f"{num1} - {num2}"
    elif op == '*':
        return f"{num1} * {num2}"
    else:
        return f"{num1} / {num2}"
