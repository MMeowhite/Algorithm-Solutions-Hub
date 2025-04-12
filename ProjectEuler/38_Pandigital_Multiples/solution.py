def pandigital_multiples():
	"""
	Question: Take the number 192 and multiply it by each of 1, 2, and 3:
		192x1=192;
		192x2=384;
		182x3=576
	By concatening each product we get the 1 to 9 pandigital, 192384576. We will
	call 192384576 the concatenated product of 192 and (1,2,3)
	The same can be achieved by starting with 9 and multiplying by 1,2,3,4 and
	5, giving the pandigital, 918273645, which is the concatenated product of 9
	and (1,2,3,4,5).
	What is the largest 1 to 9 pandigital 9-digit number that can be formed as
	the concatenated product of an integer with (1,2,3,...,n) where n > 1?
	"""
	largest_pandigital = 0
	for num in range(1, 10000):
		multipliers = 2
		while True:
			concatenated_product = compute_pandigital_number(num, multipliers)
			if len(str(concatenated_product)) > 9:
				break
			if is_pandigital_number(concatenated_product):
				largest_pandigital = max(largest_pandigital, concatenated_product)
			multipliers += 1
	return largest_pandigital


def compute_pandigital_number(number:int, multipliers:int) -> int:
	concatenated_product = ''
	for i in range(1, multipliers+1):
		concatenated_product += str(number * i)
	return int(concatenated_product)


def is_pandigital_number(number:int) -> bool:
	number_str = str(number)
	return len(number_str) == 9 and set('123456789') == set(number_str)

if __name__ == "__main__":
	print(pandigital_multiples())
