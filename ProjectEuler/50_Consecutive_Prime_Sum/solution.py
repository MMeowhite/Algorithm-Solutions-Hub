def consecutive_prime_sum(target):
	"""
	Question: The prime 41, can be written as the sum of six consecutive primes:
		41 = 2 + 3 + 5 + 7 + 11 + 13
	This is the longest consecutive primes that adds to a prime below
	one-hundred.
	The longest sum of consecutive primes below one-thousand that adds to a
	prime, contains 21 terms, and is equal to 953.
	Which prime, below one-million, can be written as the sum of the most
	consecutive primes?
	"""
	primes = generate_primes(target)
	prime_set = set(primes)
	num_primes = len(primes)

	max_length = 0
	max_prime_sum = 0
	
	# Try all possible consecutive sequences by slicing window
	for start in range(num_primes):
		sum_ = 0
		for end in range(start, num_primes):
			sum_ += primes[end]
			if sum_ >= target:
				break
			length = end - start + 1
			if sum_ in prime_set and length > max_length:
				max_length = length
				max_prime_sum = sum_

	return max_prime_sum


def generate_primes(n):
	"""Generate all primes below target"""
	sieve = [True] * n
	sieve[0:2] = [False, False]
	for i in range(2, int(n**0.5) + 1):
		if sieve[i]:
			for j in range(i * i, n , i):
				sieve[j] = False
	return [i for i, is_p in enumerate(sieve) if is_p]

def is_prime(num):
	if num <= 1:
		return False
	if num == 2: 
		return True
	if num % 2 == 0:
		return False
	for i in range(3, int(num ** 0.5) + 1, 2):
		if num % i == 0:
			return False
	
	return True


if __name__ == "__main__":
	print(consecutive_prime_sum(1000000))
