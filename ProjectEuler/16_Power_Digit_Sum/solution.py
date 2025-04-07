def power_digit_sum(exponential):
	"""
	Question: 2^15 = 32768 and the sum of its digits is 3+2+7+6+8=26.
	What is the sum of the digits of the number 2^1000?
	"""
	power_result = 2**exponential

	str_result = str(power_result)
	total = sum(int(char) for char in str_result)

	return total

if __name__ == "__main__":
	print(power_digit_sum(1000))
