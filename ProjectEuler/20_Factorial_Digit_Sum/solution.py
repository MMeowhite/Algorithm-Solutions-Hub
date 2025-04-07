def factorial_digit_sum(number):
	"""
	Question: n! means n x (n-1) x ... x 3 x 2 x 1.
	For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800
	and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27
	Find the sum of the digits in the number 100!.
	"""
	product = 1
	for i in range(1, number+1):
		product *= i
	str_product = str(product)
	total = sum(int(char) for char in str_product)

	return total

if __name__ == "__main__":
	print(factorial_digit_sum(10))
	print(factorial_digit_sum(100))
