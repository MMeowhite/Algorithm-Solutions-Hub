def convergents_of_e(n):
	"""
	Question: It's too long, please see https://projecteuler.net/problem=65
	"""
	terms = e_continued_fraction_terms(n)
	numerator, _ = compute_convergent(terms)
	return sum(int(d) for d in str(numerator))


def e_continued_fraction_terms(n):
	terms = [2]
	k = 1
	while len(terms) < n:
		terms.extend([1, 2 * k, 1])
		k += 1
	return terms[:n]

def compute_convergent(terms):
	num, den = 1, 0
	for a in reversed(terms):
		num, den = a * num + den, num
	return num, den

if __name__ == "__main__":
	print(convergents_of_e(100))
