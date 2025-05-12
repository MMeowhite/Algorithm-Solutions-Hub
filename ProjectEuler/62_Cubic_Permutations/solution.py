def cubic_permutations():
	"""
	Question: The cube, 41063625(345^3), can be permuted to product two other
	cubes: 56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the
	smallest cube which has exactly three permutations of its digits which are
	also cube.
	Find the samllest cube for with exactly five permutations of its digits are
	cube.
	"""
	cube_dict = {}
	n = 1

	while True:
		cube = n ** 3
		key = ''.join(sorted(str(cube)))

		if key in cube_dict:
			cube_dict[key].append(cube)
		else:
			cube_dict[key] = [cube]

		if len(cube_dict[key]) == 5:
			return min(cube_dict[key])
		n += 1

if __name__ == "__main__":
	print(cubic_permutations())
