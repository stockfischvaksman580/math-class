import random 
def get_random_math_problem(a, b): 
    operation = random.choice(['+', '-', '*', '/']) 
    if operation == '+': 
        return a + b 
    elif operation == '-': 
        return a - b 
    elif operation == '*': 
        return a * b 
    else: 
        return a / b