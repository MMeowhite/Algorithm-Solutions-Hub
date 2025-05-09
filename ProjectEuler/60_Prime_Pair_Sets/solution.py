def prime_pair_sets():
	"""
	Question: The primes 3, 7, 109, 673, are quite remarkable. By taking any two
	primes and concatenating them in any order the result will always be prime.
	For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of
	these four primes, 792, represents the lowest sum for a set of four primes
	with this property.
	Find the lowest sum for a set of five primes for which any two primes
	concatenate to produce another prime.
	"""
	limit = 10000
	primes = [p for p in range(2, limit) if is_prime(p)]

	pair_map = build_pair_map(primes)

	for p in pair_map:
		result = find_prime_set(pair_map, [p], 5)
		if result:
			return sum(result)
	return None

def build_pair_map(primes):
	pair_map = {}
	for i in range(len(primes)):
		for j in range(i + 1, len(primes)):
			a, b = primes[i], primes[j]
			if is_concat_prime(a, b):
				pair_map.setdefault(a, set()).add(b)
				pair_map.setdefault(b, set()).add(a)
	return pair_map

def find_prime_set(pair_map, current_set, size):
	if len(current_set) == size:
		return current_set
	for p in pair_map[current_set[-1]]:
		if all(p in pair_map.get(other, []) for other in current_set):
			result = find_prime_set(pair_map, current_set + [p], size)
			if result:
				return result
	return None

def is_prime(n):
	if n < 2: return False
	if n == 2: return True
	if n % 2 == 0: return False
	for i in range(3, int(n ** 0.5) + 1, 2):
		if n % i == 0:
			return False
	return True

def is_concat_prime(p1, p2):
	return is_prime(int(str(p1) + str(p2))) and is_prime(int(str(p2) + str(p1)))

if __name__ == "__main__":
	print(prime_pair_sets())

