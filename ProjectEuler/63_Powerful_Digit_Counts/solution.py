def powerful_digit_counts():
	"""
	Question: The 5-digit number, 168078 = 7^5, is also a fifth power.
	Similarly, the 9-digit number, 134217728 = 8^9, is a ninth power.
	How many n-digit positive integers exist which are also an n-th power?
	Math Explanation:
        - We are looking for integers of the form x^n such that:
              len(x^n) == n
        - This implies:
              10^(n-1) <= x^n < 10^n
        - Taking log base 10:
              n - 1 <= n * log10(x) < n
              (n - 1)/n <= log10(x) < 1
        - So:
              x < 10, and x >= 10^((n-1)/n)
        - Therefore:
              For each n, x ranges from 1 to 9
              (since x = 10 would produce a number with more than n digits)
        - We test x in 1 to 9 for each n starting from 1 until no x satisfies the condition.
	"""
	count = 0
	n = 1
	while True:
		found = False
		for x in range(1, 10): # only x = 1 to 9 make sense
			power = x ** n
			if len(str(power)) == n:
				count += 1
				found = True
		if not found:
			break
		n += 1

	return count

if __name__ == "__main__":
	print(powerful_digit_counts())
