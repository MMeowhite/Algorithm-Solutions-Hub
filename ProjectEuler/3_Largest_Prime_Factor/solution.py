def largest_prime_factor(target):
    """
		Question:
			The prime factors of 13195 are 5,7,13 and 29. What is the largest prime factor of the number 600851475143
		Answer: Handle Even Factors:Start by dividing the target number by 2
		until it becomes odd. This step efficiently removes all even factors and records 2 as a prime factor if applicable.
		Check for Odd Factors: Once the number is odd, iterate through potential factors starting from 3. Check each odd number up to the square root of the target. If a factor is found, divide the target by this factor and update the largest prime factor.
		Check Remaining Values: After processing all possible factors up to the square root, if the remaining value of the target is greater than 2, it is a prime number and thus the largest prime factor.
    """
    largest_prime = -1
    
    # Divide target by 2 until it's odd
    while target % 2 == 0:
        largest_prime = 2
        target = target // 2
    
    # Now target is odd, check for factors from 3 onwards
    divisor = 3
    while divisor * divisor <= target:
        while target % divisor == 0:
            largest_prime = divisor
            target = target // divisor
        divisor += 2
    
    # If remaining target is a prime number greater than 2
    if target > 2:
        largest_prime = target
    
    return largest_prime

def is_prime(number):
    """
    Check if a number is prime.
    
    Args:
        number (int): The number to check.
    
    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False

    return True

if __name__ == "__main__":
    print(largest_prime_factor(600851475143))
