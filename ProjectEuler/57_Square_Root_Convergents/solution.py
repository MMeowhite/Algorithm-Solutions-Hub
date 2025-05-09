def square_root_convergents():
	"""
	Question: It is possible to show that the square root of two can be
	expressed as an infinite continued fraction.
	By expanding this for the first four iterations, we get:
	....
	The next three expansions are 99/70, 239/169, 577/408, but the eighth
	expansion, 1393/895, is the first example where the number of digits in the
	numerator exceeds the number of digits in the denominator
	In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?
	"""
	count = 0
	numerator = 3
	denominator = 2

	for _ in range(1, 1000):
		if len(str(numerator)) > len(str(denominator)):
			count += 1

		# update numerator and denominator
		numerator, denominator = numerator + 2 * denominator, numerator + denominator
	
	return count

if __name__ == "__main__":
	print(square_root_convergents())
