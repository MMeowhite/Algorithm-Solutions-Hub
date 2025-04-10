def reciprocal_cycles(denominator):
	"""
	Question: A unit fraction contains 1 in the numerator. The dicimal
	representation of the unit fractions with denominators 2 to 10 are given:
		1/2 = 0.5
		1/3 = 0.(3)
		1/4 = 0.25
		1/5 = 0.2
		1/6 = 0.1(6)
		1/7 = 0.(142857)
		1/8 = 0.125
		1/9 = 0.(1)
		1/10 = 0.1
	Where 0.1(6) meas 0.1666666..., and has 1-digit cycle. It can be seen that
	1/7 has a 6-digit recurring cycle.
	Find the value d < 1000 for which 1/d contains the longest recurring cycle
	in its decimal fraction part
	"""
	max_length = 1
	result = 1

	for d in range(2, denominator+1):
		remainder = 1
		seen_remainders = {}
		length = 0

		while remainder != 0:
			remainder = remainder * 10
			if remainder in seen_remainders:
				length = len(seen_remainders) - seen_remainders[remainder]
				break
			seen_remainders[remainder] = len(seen_remainders)
			remainder = remainder % d
		
		if length > max_length:
			max_length = length
			result = d
	
	return result

if __name__ == "__main__":
	print(reciprocal_cycles(1000))



