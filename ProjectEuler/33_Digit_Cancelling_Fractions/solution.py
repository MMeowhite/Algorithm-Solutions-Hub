from fractions import Fraction

def digit_cancelling_fractions():
	"""
	Question: The fraction 49/98 is a curious fraction, as an inexperienced
	mathematician in attempting to simplify it may incorrectly believe that
	49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
	We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
	There are exactly for non-trivial examples of this type of fraction, less
	than one in value, and containing two digits in the numerator and
	denominator.
	If the product of these four fractions is given in its lowest common terms,
	find the value of the denominator.
	"""
	fractions = []
	for numerator in range(10, 100):
		for denominator in range(numerator + 1, 100):
			num_str = str(numerator)
			den_str = str(denominator)
			if num_str[1] == den_str[0] and den_str[1] != '0' and num_str[0] != den_str[1]:
				simplified_fraction = Fraction(numerator, denominator)
				if simplified_fraction == Fraction(int(num_str[0]), int(den_str[1])):
					fractions.append(simplified_fraction)
			if num_str[0] == den_str[1] and den_str[0] != '0' and num_str[1] != den_str[0]:
				simplified_fraction = Fraction(numerator, denominator)
				if simplified_fraction == Fraction(int(num_str[1]),int(den_str[0])):
					fractions.append(simplified_fraction)
	product = Fraction(1,1)
	for fraction in fractions:
		product *= fraction
	
	return product.denominator

if __name__ == "__main__":
	print(digit_cancelling_fractions())
