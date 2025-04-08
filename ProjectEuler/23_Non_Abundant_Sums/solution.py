def non_abundant_sums():
	"""
	Question: A perfect number is a number for which the sum of its proper
	divisors is exactly equal to the number. For example, the sum of the proper
	divisors of 28 would be 1+2+4+7+14 = 28, which means that 28 is a perfect
	number

	A number n is called deficient if the sum of its proper divisors is less
	than n and it is called abundant if this sum exceeds n.

	As 12 is the smallest abundant number, 1+2+3+4+6=16, the smallest number can
	be written the sum of two abundant numbers is 24. By mathematical analysis,
	it can be shown that all integers greater than 28123 can be written as the
	sum of two abundant numbers. However, this upper limit cannot be reduced any
	further by analysis even though it is known that the greatest number that
	cannot be expressed as the sum of two abundant numbers is less than the
	limit

	Find the sum of all the positive integers which cannot be written as the sum
	of two abundant numbers.
	"""
	abundant_numbers = []
	for i in range(1, 28124):
		if is_abundant_number(i):
			abundant_numbers.append(i)
	
	abundant_sums = set()

	# compute the sum of all two abundant number
	for i in range(len(abundant_numbers)):
			for j in range(i, len(abundant_numbers)):
				s = abundant_numbers[i] + abundant_numbers[j]
				if s <= 28123:
					abundant_sums.add(s)

	# compute the sum of all two non-abundant number
	total = 0
	for num in range(1, 28124):
		if num not in abundant_sums:
			total += num
	return total


def is_abundant_number(n):
	divisors_sums = 1 # is the divisor for all numbers
	for i in range(2, int(n**0.5)+1):
		if n % i == 0:
			if i == n // i:
				divisors_sums += i
			else:
				divisors_sums += i + n // i
	return n < divisors_sums

if __name__ == "__main__":
	print(non_abundant_sums())
