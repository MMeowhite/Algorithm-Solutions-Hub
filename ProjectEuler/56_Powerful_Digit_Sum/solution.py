def powerful_digit_sum():
	"""
	Question: A googol(10^100) is a massive number: one followed by one-hundred
													zeros; 100^100 is
													almostunimaginabley large:
													one followed by
													two-hundreded zeros.
													Despite their size, the sum
													of the digits in each number
													is only 1.
	
	considering natural numbers of the form, a^b, where a, b < 100, what is the
	maximum digital sum?
	"""
	max_digits_sum = 0
	for a in range(1, 100):
		for b in range(1, 100):
			result = a ** b
			result_str = str(result)
			digits_sum = sum(int(digit) for digit in result_str)
			if digits_sum > max_digits_sum:
				max_digits_sum = digits_sum

	return max_digits_sum

if __name__ == "__main__":
	print(powerful_digit_sum())
