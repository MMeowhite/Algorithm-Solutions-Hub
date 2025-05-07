def distinct_primes_factors():
	"""
	Question: The first two consecutive numbers have two distinct prime factors are: 
		14 = 2 x 7
		15 = 3 x 5
	The first three consecutive numbers to have three distinct prime factors
	are:
		644 = 2^2 x 7 x 23
		645 = 3 x 5 x 43
		646 = 2 x 17 x 19
	Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
	"""
	primes = generate_prime_sequence(10000000)
	for i in range(1000, 1000000):
		if (exist_distinct_prime_factors(i, primes) and 
				exist_distinct_prime_factors(i + 1, primes) and 
				exist_distinct_prime_factors(i + 2, primes) and 
				exist_distinct_prime_factors(i + 3, primes)):
			return i
	return None

def generate_prime_sequence(max_number):
	"""Generate a prime sequence to store primes."""
	primes = [True for _ in range(max_number + 1)]
	p = 2
	while p * p <= max_number:
		if primes[p]:
			for i in range(p * p, max_number + 1, p):
				primes[i] = False
		p += 1
	prime_numbers = [p for p in range(2, max_number + 1) if primes[p]]
	return prime_numbers
	
def exist_distinct_prime_factors(num, primes):
	distinct_factors = set()
	for prime in primes:
		if prime * prime > num:
			break
		while num % prime == 0:
			distinct_factors.add(prime)
			num //= prime
	if num > 1:
	 	distinct_factors.add(num)
	return len(distinct_factors) == 4


if __name__ == "__main__":
	print(distinct_primes_factors())
