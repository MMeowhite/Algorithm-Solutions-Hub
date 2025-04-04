def summation_of_primes(target):
	"""
	Question: The sum of the primes below 10 is 2+3+5+7 = 17.Find the sum of all
	primes below two million.
	"""
	sum = 0
	for i in range(1, target+1):
		if is_prime(i):
			sum = sum + i
	return sum

def is_prime(number):
	if number <= 1:
		return False
	if number == 2:
		return True
	if number % 2 == 0:
		return False

	for i in range(3, int(number ** 0.5)+1, 2):
		if number % i == 0:
			return False

	return True

if __name__ == "__main__":
	print(summation_of_primes(10))
	print(summation_of_primes(2000000))
