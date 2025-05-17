def print_pattern(n):
    """
    This function prints a pattern of asterisks (*) on the console.
    The number of asterisks in the pattern is determined by the input parameter 'n'.
    
    Example usage:
    >>> print_pattern(4)
    *
   ***
  *****
"""
    for i in range(1, n + 1):
        # Print horizontal lines
        for j in range(n - 2*i):
            print(" ", end="")
        # Print asterisks for the current line
        if i % 2 == 0:
            print("*" * (i+1))
        else:
            print("*" * (n-i-1))

# Example usage: Print a pattern with 5 asterisks
print_pattern(5)
