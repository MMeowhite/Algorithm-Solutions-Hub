def combinatoric_selections(threshold):
	"""
	Question: There are exactly ten ways of selecting three from five, 12345:
		123, 124, 125, 134, 135, 145, 234, 235, 245, 345
	In combinatorics, we use the notation, (5 3) = 10.
	In general, (n r) = n!/r!*(n - r)!, where r <= n, n! = n * (n -1) * (n -2) * (n - 3) * ...* 3 * 2 * 1 and 0! = 1.
	It is not until n = 23, that a value exceeds one-million: (23 10) = 114406.
	How many, not necessarily distinct, values of (n r) for 1 <= n <= 100, are greater than one-million?
	"""
	total = 0
	for n in range(1, 101):
		# r is less or equal to n
		for r in range(1, n + 1):
			result = compute_combination(n , r)
			if result > threshold:
				total += 1
	return total
		

def compute_combination(n, r):
	from math import factorial
	return factorial(n) // (factorial(r)*(factorial(n - r)))


if __name__ == "__main__":
	print(combinatoric_selections(1000000))

