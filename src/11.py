import random

def get_random_code():
    operations = ["+", "-", "*", "/"]
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operation = random.choice(operations)
    answer = eval(f"{num1} {operation} {num2}")
    return f"What is {num1} {operation} {num2}?"