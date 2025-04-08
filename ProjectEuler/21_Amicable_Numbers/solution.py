def amicable_numbers(end):
	"""
	Question: Let d(n) be defined as the sum of proper divisors of n (numbers
			less than n which divide evenly into n).
	if d(a)=b and d(b)=a, where a is not equal to b, then a and b are an
	amicable pair and each of a and b are called amicable numbers.
	For example, the proper divisors of 220 are 1,2,4,5,10,11,20,22,44,55 and
	110; there for d(220)=284.The proper divisors of 284 are 1,2,4,71 and 142;
	so d(284)=220.
	Evaluate the sum of all the amicable numbers under 10000.
	"""
	total_list = []
	# to reduce the compute frequency, find whether duplicated in the total_list
	for i in range(2, end+1):
		if i in total_list:
			continue
		# the target is not in total_list
		amicable_number = find_amicable_numbers(i)
		if amicable_number != -1:
			total_list.append(i)
			total_list.append(amicable_number)
	
	return sum(number for number in total_list)


def find_amicable_numbers(source):
	"""
	Find the amicable_numbers given sorce
	"""
	target = compute_divisors_sum(source)
	if is_amicable_numbers(target, source):
		return target
	else:
	 	return -1


def is_amicable_numbers(a, b):
	"""
	Determine a pair of numbers are amicable numbers or not
	"""
	if a == b:
		return False

	return (optimal_compute_divisors_sum(a) == b) and (a == optimal_compute_divisors_sum(b))

def compute_divisors_sum(number):
	"""
	Compute the sum of the all divisors less than nubmer itself
	"""
	total = 1 # 1 is divisor for all numbers
	for i in range(2, number // 2 + 1):
		if number % i == 0:
			total += i

	return total

def optimal_compute_divisors_sum(number):
	total = 1 # 1 is divisor for all numbers
	for i in range(2, int(number**0.5) + 1):
		if number % i == 0:
			if i == number // i:
				total += i
			else:
				total += i + number // i
	return total
				

if __name__ == "__main__":
	# testing function
	print(optimal_compute_divisors_sum(284))
	print(optimal_compute_divisors_sum(220))
	print(is_amicable_numbers(284, 220))
	print(find_amicable_numbers(220))
	print(find_amicable_numbers(284))
	# print the result
	print(amicable_numbers(10000))
