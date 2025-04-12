def double_base_palindromes(target):
	"""
	Question: The decimal number, 585=1001001001(binary), is palindromic in both
	cases.
	Find the sum of all numbers, less than one million, which are palindromic in
	base 10 and base 2.
	"""
	total = 0
	for i in range(target + 1):
		if is_palindromes_in_both_base_2_and_10(i):
			total += i
	return total


def is_palindromes_in_both_base_2_and_10(num):
	"""Determine a number is a palindromes or not"""
	num_str = str(num)
	num_base_2 = base_2(num)

	return num_str == num_str[::-1] and num_base_2 == num_base_2[::-1]



def base_2(num):
	"""
	Converts a decimal number to its binary representation
	"""
	if num == 0:
		return "0"
	binary_digits = []
	while num > 0:
		remainder = num % 2 # get the remainder 0 or 1
		binary_digits.append(str(remainder)) # appende the remainder to the list
		num //= 2 # integer division by 2
	
	# The binary digits are in reverse order, so reverse them before joinin them 
	binary_digits.reverse()
	return ''.join(binary_digits)


if __name__ == "__main__":
	print(double_base_palindromes(1000000))
