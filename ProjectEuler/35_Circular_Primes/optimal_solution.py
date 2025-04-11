def sieve_of_eratosthenes(limit):
    """
    Generates all prime numbers up to a given limit using the Sieve of Eratosthenes algorithm.

    :param limit: The upper bound for generating prime numbers.
    :return: A list of prime numbers up to the given limit.
    """
    is_prime = [True] * (limit + 1)  # Initialize a list to track prime status of numbers
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers

    p = 2  # Start with the first prime number
    while p * p <= limit:  # Only need to check up to the square root of the limit
        if is_prime[p]:  # If p is a prime number
            for i in range(p * p, limit + 1, p):  # Mark multiples of p as non-prime
                is_prime[i] = False
        p += 1

    # Return a list of all numbers that are still marked as prime
    return [p for p in range(2, limit + 1) if is_prime[p]]

def is_prime_after_change(num, prime_set):
    """
    Checks if all rotations of a number's digits are prime.

    :param num: The number to check.
    :param prime_set: A set of prime numbers for quick lookup.
    :return: True if all rotations are prime, False otherwise.
    """
    num_str = str(num)  # Convert the number to a string for easy rotation
    for i in range(len(num_str)):  # Iterate through all possible rotations
        rotated_num = int(num_str[i:] + num_str[:i])  # Rotate the number
        if rotated_num not in prime_set:  # Check if the rotated number is prime
            return False
    return True

def circular_primes(target):
    """
    Counts all circular primes below a given target.

    :param target: The upper bound for finding circular primes.
    :return: The count of circular primes below the target.
    """
    primes = sieve_of_eratosthenes(target)  # Generate all primes up to the target
    prime_set = set(primes)  # Convert the list of primes to a set for quick lookup
    counts = 0  # Initialize the count of circular primes

    for prime in primes:  # Iterate through all generated primes
        if is_prime_after_change(prime, prime_set):  # Check if the prime is circular
            counts += 1  # Increment the count if it is a circular prime

    return counts

if __name__ == "__main__":
    print(circular_primes(1000000))  # Output should be 55`
