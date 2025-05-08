def permuted_multiples():
	"""
	Question: It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order. 
	Find the samllest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
	contain the same digits
	"""
	x = 1
	while True:
		multiples = [x * i for i in range(1, 7)]
		if check_digits(multiples):
			return x
		x += 1
		


def check_digits(nums:list) -> bool:
	"""Given the a list, determine if each element of the list contains the same digits"""
	sorted_digits = sorted(str(nums[0]))
	for num in nums:
		if sorted(str(num)) != sorted_digits:
			return False
	return True

if __name__ == "__main__":
	print(permuted_multiples())
