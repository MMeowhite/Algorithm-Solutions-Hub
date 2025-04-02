def largest_palindrome_product(digit):
	lower_bound = 10**(digit-1)
	upper_bound = 10**digit
	
	max_palindrome_product = 0
	for i in range(lower_bound, upper_bound):
		for j in range(lower_bound,upper_bound):
			current_product = i * j
			if str(current_product) == str(current_product)[::-1]:
				max_palindrome_product = max_palindrome_product if max_palindrome_product > current_product else current_product
	
	return max_palindrome_product


if __name__ == "__main__":
	print(largest_palindrome_product(3))
