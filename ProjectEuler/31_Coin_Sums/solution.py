def coin_sums(target):
	"""
	Question: In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:
	1p, 2p, 5p, 10p, 20p, 50p, 100p, and 200p
	It is possible to make 200 in the following way:
	1xe1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
	How many different ways can e2 be made using any number of coins?
	"""
	coins = [1, 2, 5, 10, 20, 50, 100, 200]
	ways = [0] * (target + 1)
	ways[0] = 1 # There is 1 way to make 0 pence (use no coins)

	for coin in coins:
		for amount in range(coin, target + 1):
			ways[amount] += ways[amount - coin]
	return ways[target]

if __name__ == "__main__":
	print(coin_sums(200))
	
