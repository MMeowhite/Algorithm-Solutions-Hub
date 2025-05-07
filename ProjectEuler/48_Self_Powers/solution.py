def self_powers():
	"""
	Question: The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
	Find the last ten digits of these series:
		1^1 + 2^2 + 3^3 + ... + 1000 ^ 1000
	"""
	total = 0
	for i in range (1, 1001):
		total += i**i
	total_str = str(total)
	return total_str[-10:]


if __name__ == "__main__":
	print(self_powers())
