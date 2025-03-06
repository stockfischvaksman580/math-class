import random

def get_random_problem():
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)
    op = random.choice(["+", "-", "*", "/"])
    problem = f"{num1} {op} {num2}"
    answer = eval(problem)
    return problem, answer
