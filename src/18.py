def square_root(x):
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number")
    elif x == 0:
        return 0
    else:
        return x ** 0.5

# Example usage:
print(square_root(16))  # Output: 4.0
print(square_root(-9))  # Raises ValueError: Cannot compute square root of a negative number
