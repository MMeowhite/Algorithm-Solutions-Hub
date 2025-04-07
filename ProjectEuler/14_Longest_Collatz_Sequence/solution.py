def longest_collatz_sequence(target):
	"""
	Question: the following iterative sequence is defined for the set of
	positive integers:
		n -> n/2 (n is even)
		n -> 3n + 1 (n is odd)
	using the rule above and starting with 13, we generate the following
	sequence:
		13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
	It can be seen that this sequence (starting at 13 and finishing at 1)
	contains 10 terms. Although it has not bben proved(Collatz Problem), it is
	thought that all starting numbers finish at 1.
	Which starting number, under one million, produces the longest chain?
	Note: Once the chain starts the terms are allowed to go above one million.
	"""
	max_count = 0
	index = 1 # compute the collatz sequence from 1
	while index < target:
		current_count, stop = compute_collatz_sequence(0, index)
		if stop != 1:
			raise ValueError("The stop number must be 1")
		if current_count > max_count:
			max_count = current_count
		index += 1

	return max_count

def compute_collatz_sequence(count, number):
	count += 1
	if number == 1:
		return count, 1
	
	if number % 2 == 0:
		# the number is even
		return compute_collatz_sequence(count, number / 2)
	else:
		# the number is odd
		return compute_collatz_sequence(count, 3*number + 1)

if __name__ == "__main__":
	print(compute_collatz_sequence(0, 13))
	print(longest_collatz_sequence(1000000))
