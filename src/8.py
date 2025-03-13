import random

def solve_math_problem(problem):
    numbers = problem.split(" ")
    operation = numbers[-1]
    numbers = [int(n) for n in numbers[:-1]]
    result = 0
    if operation == "+":
        result = sum(numbers)
    elif operation == "-":
        result = numbers[0] - numbers[1]
    elif operation == "*":
        result = numbers[0] * numbers[1]
    elif operation == "/":
        result = numbers[0] / numbers[1]
    return str(result)

def generate_math_problem():
    numbers = [random.randint(1, 10) for _ in range(2)]
    operation = random.choice(["+", "-", "*", "/"])
    problem = " ".join([str(n) for n in numbers]) + " " + operation
    return problem

problem = generate_math_problem()
print(solve_math_problem(problem))
