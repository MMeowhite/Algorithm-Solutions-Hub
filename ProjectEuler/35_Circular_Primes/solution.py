def circular_primes(target):
	"""
	Question: The number, 197, is called a circular prime because all rotations
	of the digits: 197, 971, and 719, are themselves prime.
	There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37,
	71, 73, 79, 97.
	How many circular primes are there below one million?
	"""
	counts = 0
	for i in range(2, target):
		if is_prime(i) and is_prime_after_change(i):
			counts += 1
			
	return counts


def is_prime(number):
	if number <= 1:
		return False
	if number == 2:
		return True
	if number % 2 == 0:
		return False
	for i in range(3, int(number**0.5) + 1, 2):
		if number % i == 0:
			return False
	return True

def is_prime_after_change(num):
	num_str = str(num)
	for i in range(len(num_str)):
		rotated_num = int(num_str[i:] + num_str[:i])
		if not is_prime(rotated_num):
			return False
	return True

if __name__ == "__main__":
	print(circular_primes(1000000)) 
