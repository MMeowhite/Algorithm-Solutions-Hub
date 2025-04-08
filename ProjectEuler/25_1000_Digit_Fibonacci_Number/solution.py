import math

def thousand_digit_fibonacci_number(digits):
	"""
	Question: The fibonacci sequence is defined by the recurrence relation:
		Fn = Fn-1 + Fn_2 where F1 = 1 and F2 = 1
	What is the index of the first term in Fibonacci sequence to contain 1000
	digits
	"""
	fibonacci_terms = [1, 1, 2]
	current_index = 3 # current index of third term of fibonacci sequence
	while True:
		next_term = fibonacci_terms[2] + fibonacci_terms[1]
		current_index += 1

		if (int(math.log10(next_term)) + 1) == digits:
			return current_index

		# update fibonacci sequence
		fibonacci_terms[0] = fibonacci_terms[1]
		fibonacci_terms[1] = fibonacci_terms[2]
		fibonacci_terms[2] = next_term
		

if __name__ == "__main__":
	print(thousand_digit_fibonacci_number(3))
	print(thousand_digit_fibonacci_number(1000))
