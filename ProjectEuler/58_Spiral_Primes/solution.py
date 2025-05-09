def spiral_primes():
	"""
	Question: Starting with the number 1 at the center, a square spiral is formed by moving in an anticlockwise direction. As layers are added, the spiral grows with side lengths of 3, 5, 7, etc.

For example, a 7×7 spiral looks like this:
	37 36 35 34 33 32 31  
38 17 16 15 14 13 30  
39 18  5  4  3 12 29  
40 19  6  1  2 11 28  
41 20  7  8  9 10 27  
42 21 22 23 24 25 26  
43 44 45 46 47 48 49  
	We observe that: The diagonals of the spiral contain numbers such as 1, 3, 5, 7, 9, 13, 17, 21, etc. Some of these diagonal numbers are prime numbers.
	Find the side length of the square spiral for which the ratio of prime numbers along both diagonals first falls below 10%.
	"""
	prime_count = 0
	total_diagonals = 1
	side_length = 1
	current_number = 1

	while True:
		side_length += 2
		for _ in range(4):
			current_number += side_length - 1
			if is_prime(current_number):
				prime_count += 1
		total_diagonals += 4

		# compute prime ratio
		ratio = prime_count / total_diagonals
		if ratio < 0.10:
			return side_length


def is_prime(num):
	if num < 2:
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
	print(spiral_primes())


