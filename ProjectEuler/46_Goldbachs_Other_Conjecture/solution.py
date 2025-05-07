def goldbachs_other_conjecture():
	"""
	Question: It was proposed by Christian Goldbach that every odd composite
	number can be written as the sum of a prime and twice a squre:
		9 = 7 + 2 x 1^2
		15 = 7 + 2 x 2^2
		21 = 3 + 2 x 3^2
		25 = 7 + 2 x 3^2
		27 = 19 + 2 x 2^2
		33 = 31 + 2 x 1^2
	It turns out that the conjecture was false.
	What is the smallest odd composite that cannot be written as the sum of a
	prime and twice a square?
	"""
	n = 9
	while True:
		if not is_prime(n):
			found = False
			for k in range(1, int((n // 2) ** 0.5) + 1):
				if is_prime(n - 2 * k * k):
					found = True
					break
			if not found:
				return n 
		n += 2

def is_prime(n):
	if n <= 1:
		return False
	if n == 2:
		return True
	if n % 2 == 0:
		return False
	for i in range(3, int(n ** 0.5) + 1, 2):
		if n % i == 0:
			return False
	return True


if __name__ == "__main__":
	print(goldbachs_other_conjecture())
