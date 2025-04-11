import math

def digit_factorials():
	"""
	Question: 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145
	Find the sum of all numbers which are equal to the sum of the factorial of
	their digits.
	Note: As 1! = 1 and 2! = 2 are not sums they are not included
	"""
	# Precompute the factorials of digits 0-9
	factorials = {str(i): math.factorial(i) for i in range(10)}

	# Initialize the sum of curious numbers
	curious_sum = 0

	# Upper bound for the search
	# The maximum possible sum of factorials for a number with n digits is 9! * n
	# For example, for a 7-digit number, the maximum sum is 9! * 7 = 2540160
	# We can safely set an upper bound of 10^6 (1,000,000) for this problem
	upper_bound = 1000000

	# Iterate through all numbers from 3 to the upper bound
	for num in range(3, upper_bound):
		# Convert the number to a string to easily access each digit
		num_str = str(num)
		# Calculate the sum of the factorials of the digits
		factorial_sum = sum(factorials[digit] for digit in num_str)
		# Check if the number is equal to the sum of the factorials of its digits
		if num == factorial_sum:
			curious_sum += num

	return curious_sum

if __name__ == "__main__":
	print(digit_factorials())
