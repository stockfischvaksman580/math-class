def add_numbers(a, b):
    return a + b

def multiply_numbers(a, b):
    return a * b

def subtract(numbers1, numbers2):
    result = numbers1 - numbers2
    return result

def divide_numbers(numbers1, numbers2):
    if numbers2 == 0:
        raise ValueError("Cannot divide by zero")
    return numbers1 / numbers2
