def digit_fifth_powers(digits):
	"""
	Surprisingly there are only three numbers that can be written as the sum of
	fourth powers of their digits:
		1634 = 1^4 + 6^4 + 3^4 + 4^4
		8208 = 8^4 + 2^4 + 0^4 + 8^4
		9474 = 9^4 + 4^4 + 7^4 + 4^4
	As 1 = 1^4 is not a sum it is not included
	The sum of these numbers is 1634 + 8208 + 9474 = 19316
	Find the sum of all the numbers that can be written as the sum of fifth
	opwers of their digits
	"""
	upper_boundary = 6 * (9 ** 5) # n x 9^5 < 10^(n-1)
	
	result = []
	for num in range(2, upper_boundary):
		if is_sum_of_powers(num, digits):
			result.append(num)
	return sum(result)

def is_sum_of_powers(number, powers):
	total = 0
	temp = number
	while temp > 0:
		digit = temp % 10
		total += digit ** powers
		temp //= 10
	return total == number

if __name__ == "__main__":
	print(digit_fifth_powers(5))
