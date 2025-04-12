def truncatable_primes(target):
	"""
	Question: The number 3797 has an interesting property. Being prime itself,
	it is possible to continuously remove digits from left to right, and reamin
	prime at each stage: 4797,797,97,and 7.Similarly we can work from right to
	left: 3797, 379, 37, and 3.
	Fine the sum of the only eleven primes that are both truncable from left to
	right to left.
	"""
	count = 0
	total = 0
	primes = sieve_of_eratosthenes(1000000)
	primes_set = set(primes)
	for prime in primes:
		if prime < 10:
			continue
		if is_truncatable_primes(prime, primes_set):
			total += prime
			count += 1
			if count == target:
				break
	return total
	

def is_truncatable_primes(number, primes_set):
	number_str = str(number)
	for i in range(len(number_str)):
		# Check left-to-right truncation
		if int(number_str[i:]) not in primes_set:
			return False
		if int(number_str[:len(number_str) - i]) not in primes_set:
			return False

	return True


def sieve_of_eratosthenes(limit):
	is_prime = [True] * (limit + 1)
	is_prime[0] = is_prime[1] = False
	p = 2
	while p * p <= limit:
		if is_prime[p]:
			for i in range(p * p, limit + 1, p):
				is_prime[i] = False
		p += 1
	return [p for p in range(2, limit + 1) if is_prime[p]]

if __name__ == "__main__":
	print(truncatable_primes(11))
