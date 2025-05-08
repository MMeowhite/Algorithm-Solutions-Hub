def prime_digit_replacements(family_size):
	"""
	Question: By replacing the 1st digit of 2-digit number *3, it turns out that
	six of nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
	By replacing the 3rd and 4th digits of 56**3 with the same digit, this
	5-digit number is the first example having seven primes among the ten
	generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663,
	56773, and 56993. Consequently 56003, being the first member of this family,
	is the smallest prime with this property.
	Find the smallest prime which, by replacing part of the number(not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
	"""
	num = 11
	while True:
		# skip the even number
		if not is_prime(num):
			num += 2
			continue
		s = str(num)
		patterns = generate_patterns(len(s))
		for pattern in patterns:
			prime_count = 0
			smallest = None
			for d in range(10):
				# skip the 0 in the first digit
				if 0 in pattern and d == 0:
					continue
				new_num_str = replace_digits(s, pattern, d)
				new_num = int(new_num_str)
				if is_prime(new_num):
					prime_count += 1
					if smallest is None:
						smallest = new_num
			if prime_count == family_size:
				return smallest
		num += 2

def is_prime(n):
	if n < 2:
		return False
	if n == 2:
		return True
	if n % 2 == 0:
		return False
	for i in range(3, int(n ** 0.5) + 1, 2):
		if n % i == 0:
			return False
	return True


def generate_patterns(length):
	patterns = []
	for size in range(1, length):
		def helper(start, current):
			if len(current) == size:
				patterns.append(current[:])
				return 
			for i in range(start, length):
				current.append(i)
				helper(i + 1, current)
				current.pop()
		helper(0, [])
	return patterns


def replace_digits(s, indexes, digit):
	s = list(s)
	for i in indexes:
		s[i] = str(digit)
	return ''.join(s)


if __name__ == "__main__":
	print(prime_digit_replacements(8))
