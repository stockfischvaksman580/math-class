import numpy as np

def find_prime_numbers(n):
    """
    This function finds all prime numbers less than or equal to n.
    
    Args:
        n (int): An integer representing the upper limit for prime numbers.
        
    Returns:
        list: A list of prime numbers up to n.
    """
    sieve = np.ones(n+1, dtype=bool)
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            sieve[2*i::i] = [False] * ((n-2*i-1)//i + 1)
    
    return [2*i + 3 if i == 2 else i for i in range(4, n+1, 2) if (sieve[i])]
