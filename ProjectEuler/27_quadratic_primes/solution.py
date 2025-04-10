def quadratic_primes():
	"""
	Question: Eluer discovered the remarkable quadratic formula:
		n^2 + n + 41
	It turns out that the formula will product 40 primes for the consecutive
	integer values 0 <= n <= 39. However, when n = 40, 40^2+40+41 = 40(40+1) +
	41 is divisble by 41, and certainly when n = 41, 41^2+41+41 is clearly
	divisble by 41.
	The incredible formula n^2-79n+1601 was discovered, which produces 80 primes
	for consecutive values 0 <= n <= 79. The product of the cofeeicients, -79
	and 1601, is -126479.
	Considering quadratics of the form:
		n^2+an+b, where |a| < 1000 and |b| <= 1000
	where |n| is the modulus/absolute value of n e.g. |11| = 11, and |-4| = 4
	Find the product of the cofficients, a and b, for the quadratic expression
	that produces the maximum number of primes for consecutive values of n,
	starting with n = 0.
	"""
	max_primes = 0
	max_a = 0
	max_b = 0

	for a in range(-999, 1000):
		for b in range(-1000, 1001):
			n = 0
			current_primes = 0
			while True:
				value = n * n + a * n + b
				if value < 2:
					break
				if is_prime(value):
					current_primes += 1
				else:
				 	break
				n += 1
			if current_primes > max_primes:
			  	max_primes = current_primes
			  	max_a = a
			  	max_b = b

	return max_a * max_b

def is_prime(n):
	"""
	Determine a number is a prime or not
	"""
	if n <= 1:
		return False
	if n <= 2:
		return True
	for i in range(3, int(n**0.5)+1, 2):
		if n % i == 0:
			return False
	
	return True
if __name__ == "__main__":
	print(quadratic_primes())
