def pandigital_products():
	"""
	Question: We shall say that an n-digit number is pandigital if it makes use
	of all the digits 1 to n exactly once; for example, the 5-digit number,
	15234, is 1 through 5 pandigital
	The product 7254 is unusual, as the identity, 39x186=7254, containing
	multiplicand, multiplier, and product is 1 through 9 pandigital.
	Find the sum of all products whose multiplicand/multiplier/product identity
	can be written as a 1 through 9 pandigital.
	HINT:Some products can be obtained in more than one way so be sure to only
	include it once in your sum.
	"""
	products = set() # Use a set to avoid duplicates

	# Iterate over possible lengths of multiplicand and multiplier
	for i in range(1, 100): # Multiplicand can be 1 to 2 digits
		for j in range(1, 10000): # Multiplier can be 1 to 4 digits
			product = i * j
			concatenated = str(i) + str(j) + str(product)
			if len(concatenated) == 9 and is_pandigital(concatenated):
				products.add(product)
	
	return sum(products)


def is_pandigital(s):
	"""Check if the string s is a 1 through 9 pandigital nunber."""
	return len(s) == 9 and set(s) == set('123456789')

if __name__ == "__main__":
	print(pandigital_products())
