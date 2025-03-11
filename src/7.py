import random

def solve_math_problem(n):
    if n == 1:
        return "2 + 3"
    elif n == 2:
        return "5 * 4"
    else:
        return str(random.randint(0, 10)) + " / " + str(random.randint(0, 10))
