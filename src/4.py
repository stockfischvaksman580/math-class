def generate_math_problem(n):
    numbers = [random.randint(1, 10) for i in range(n)]
    operations = ['+', '-', '*', '/']
    operation = random.choice(operations)
    problem = f"{numbers[0]} {operation} {numbers[1]} = "
    answer = numbers[0] + numbers[1]
    return problem, answer
