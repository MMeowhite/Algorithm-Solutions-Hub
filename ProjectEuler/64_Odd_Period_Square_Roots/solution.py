import math

def odd_period_square_roots(limit):
	"""
	Question: It too long, please see https://projecteuler.net/problem=64
	"""
	count = 0
	for N in range(2, limit + 1):
		if int(math.isqrt(N)) ** 2 == N:
			continue
		if period_length_of_sqrt(N) % 2 == 1:
			count += 1
	return count
	

def period_length_of_sqrt(N):
	a0 = int(math.isqrt(N))
	if a0 * a0 == N:
		return 0

	m, d, a = 0, 1, a0
	period = 0

	seen = set()
	while True:
		m = d * a - m
		d = (N - m * m ) // d
		a = (a0 + m) // d
		period += 1

		if a == 2 * a0:
			break
		
	return period

if __name__ == "__main__":
	print(odd_period_square_roots(10000))
