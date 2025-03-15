
import random

def get_random_python_code():
    operators = ["+", "-", "*", "/"]
    variables = ["x", "y", "z"]
    functions = ["sin", "cos", "tan"]
    
    operator = random.choice(operators)
    variable1 = random.choice(variables)
    variable2 = random.choice(variables)
    function = random.choice(functions)
    
    return f"{function}({variable1} {operator} {variable2})"