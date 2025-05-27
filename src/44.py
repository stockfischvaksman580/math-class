import math

def calculate_area_rectangle(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    print(f"Rectangle area: {area}")
    print(f"Rectangle perimeter: {perimeter}")

def check_square(side_length):
    if side_length >= 0:
        return True
    else:
        return False

# Example usage
calculate_area_rectangle(10, 5)  # Example with a square
check_square(-5)
