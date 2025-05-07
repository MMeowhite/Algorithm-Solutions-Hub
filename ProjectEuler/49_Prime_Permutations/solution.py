def prime_permutations():
	"""
	Question: The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
	There are no arithmetic sequences made up of three 1-, 2-, 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.
	What 12-digit number do you form by concatenating the three terms in this sequence?
	"""
	# Generate all 4-digit primes
	primes = [i for i in range(1000, 10000) if is_prime(i)]

	# Group by permutations
	perm_groups = {}
	for p in primes:
		key = ''.join(sorted(str(p)))
		if key in perm_groups:
			perm_groups[key].append(p)
		else:
			perm_groups[key] = [p]

	# Search for valid arithmetic sequences
	for key in perm_groups:
		group = sorted(perm_groups[key])
		n = len(group)
		if n < 3:
			continue
		for i in range(n):
			for j in range(i + 1, n):
				a = group[i]
				b = group[j]
				diff = b - a
				c = b + diff
				if c in group:
					if a == 1487 and b == 4817 and c == 8147:
						continue
					return str(a) + str(b) + str(c)
	return "Null"


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
	print(prime_permutations())
