def nst_prime(target):
    """
    Question: By listing the first six prime numbers: 2,3,5,7,11 and 13, we can
    see that the 6th prime is 13. What is the 10001st prime number?
    """
    index = 0
    prime_number = 2  # from the first prime number
    candidate = 2     # check each number form the start is prime or not

    while index < target:
        if is_prime(candidate):
            index += 1
            prime_number = candidate
        candidate += 1

    return prime_number

def is_prime(number):
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
    print(nst_prime(6))
    print(nst_prime(10001))
