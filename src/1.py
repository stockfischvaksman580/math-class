import random

def get_random_math_problem():
    operands = [10, 20, 30, 40, 50]
    operation = ["+", "-", "*", "/"]
    problem = f"{operands[random.randint(0, len(operands) - 1)]} {operation[random.randint(0, len(operation) - 1)]} {operands[random.randint(0, len(operands) - 1)]}"
    return problem
