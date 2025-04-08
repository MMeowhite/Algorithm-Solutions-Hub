import math

def lexicographic_permutations(index):
	"""
	Question: A permutation is an ordered arrangement of objects. For example,
	3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the
	permutations are listed numerically or alphabetically, we call it
	lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
		012 021 102 120 201 210
	What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4,
	5, 6, 7, 8 and 9?
	"""
	digits = list(range(10))
	result = []
	index -= 1
	for i in range(10):
		factorial = math.factorial(9 - i)
		pos = index // factorial
		result.append(str(digits[pos]))
		digits.pop(pos)
		index = index % factorial

	return ''.join(result)

if __name__ == "__main__":
	print(lexicographic_permutations(1000000))
