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
	contains 10 terms. Although it has not bben proved(Collatz Problem), it is thought that all starting numbers finish at 1.
	Which starting number, under one million, produces the longest chain?
	Note: Once the chain starts the terms are allowed to go above one million
	"""
    max_count = 0
    max_number = 1
    cache = {}  # Cache to store the length of Collatz sequences for numbers

    for index in range(1, target):
        current_count = compute_collatz_sequence(index, cache)
        if current_count > max_count:
            max_count = current_count
            max_number = index

    return max_number, max_count

def compute_collatz_sequence(number, cache):
    """
    Compute the length of the Collatz sequence starting from 'number' using memoization.
    """
    if number == 1:
        return 1
    if number in cache:
        return cache[number]
    
    if number % 2 == 0:
        next_number = number // 2
    else:
        next_number = 3 * number + 1
    
    cache[number] = 1 + compute_collatz_sequence(next_number, cache)
    return cache[number]

if __name__ == "__main__":
    print(longest_collatz_sequence(1000000))
