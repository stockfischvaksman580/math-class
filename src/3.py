
def math_problem():
    # Generate two random numbers between 1 and 10
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    
    # Print the problem statement
    print(f"What is {num1} + {num2}?")
    
    # Get the user's answer
    answer = int(input())
    
    # Check if the answer is correct
    if answer == num1 + num2:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is", num1 + num2)