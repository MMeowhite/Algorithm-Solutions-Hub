def champernownes_constant():
	"""
	Question: An irrational decimal fraction is created by concatenating the
	positive integers:
		0.123456789101112131415161718192021...
	It can be seen that the 12th digit of the fraction part is 1.
	if dn represents nth digit of the fraction part, find the value of the
	following expression:
		d_1 x d_10 x d_100 x d_1000 x d_10000 x d_100000 x d_1000000
	"""
	# generate champernowne's constant
	constant = ''.join(str(i) for i in range(1,10000001))
	
	# extract the required digits
	positions = [1, 10, 100, 1000, 10000, 100000, 1000000]
	digits = [int(constant[pos - 1]) for pos in positions]

	# calculate the product of the digits
	product = 1
	for digit in digits:
		product *= digit
	
	return product

if __name__ == "__main__":
	print(champernownes_constant())
