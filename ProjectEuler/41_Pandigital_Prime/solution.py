import itertools

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n**0.5) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False   
    return True

def find_largest_pandigital_prime():
    """Find the largest n-digit pandigital prime."""
    # We'll start from the largest possible n (9) and work our way down
    for n in range(9, 0, -1):
        digits = list(map(str, range(1, n+1)))
        # Generate all permutations of the digits
        permutations = itertools.permutations(digits)
        # Convert permutations to integers and sort them in descending order
        candidates = sorted([int(''.join(p)) for p in permutations], reverse=True)
        # Check each candidate for primality
        for candidate in candidates:
            if is_prime(candidate):
                return candidate
    return None

if __name__ == "__main__":
    largest_pandigital_prime = find_largest_pandigital_prime()
    print(f"The largest pandigital prime is: {largest_pandigital_prime}")
