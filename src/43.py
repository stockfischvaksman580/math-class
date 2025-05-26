def find_greatest_product(a: list, b: list) -> int:
    """
    This function takes two lists of positive integers and returns their greatest common product.
    
    Example usage:
    >>> find_greatest_product([4, 5], [6, 1])
    20
    """
    # Multiply the elements of both lists
    greatest_product = a * b
    
    return greatest_product

# Check function to verify the correctness of the solution
def check_solution():
    assert find_greatest_product([4, 5], [6, 1]) == 20, "Test case 1 failed"
    print("Solution is correct!")

check_solution()
