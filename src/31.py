def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Example usage:
numbers = [12, 4, 5, 6, 7, 3, 8, 9, 10]
sorted_numbers = quicksort(numbers)
print(sorted_numbers)
