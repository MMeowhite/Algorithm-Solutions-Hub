def sum_square_difference(target):
	"""
		Question: The sum of the squares of the first ten natural number is, 1^2 + 2^2 +
		... + 10^2 = 385. The square of the sum of the first natural number is
		(1+2+...+10)^2 = 55^2 = 3025. Hence the difference between the sum of
		squares of the first ten natural number and the square of the sum is
		3025-385 = 2640
		Find the difference between the sum of the squares of the first one
		hundred natural numbers and the square of the sum.
	"""
	sum_of_squares = 0
	squares_of_sum = 0
	for i in range(1, target+1):
		sum_of_squares += i**2
		squares_of_sum += i
	squares_of_sum = squares_of_sum**2
	difference = squares_of_sum - sum_of_squares

	return difference

if __name__ =="__main__":
	print(sum_square_difference(100))
