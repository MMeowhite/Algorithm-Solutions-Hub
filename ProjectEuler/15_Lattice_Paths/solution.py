def lattice_paths(rows, cols):
	"""
	Starting in the top left corner of a 2x2 grid, and only being able to move
	to the right and down, there are exactly 6 routes to the bottom right corner
	How many such routes are there through a 20x20 grid?
	"""
	# initiate a zreos-grid with given rows and cols
	grid = [[0 for _ in range(cols)] for _ in range(rows)]
	
	# setting boundary condition
	for i in range(rows):
		grid[i][0] = 1
	for j in range(cols):
		grid[0][j] = 1

	for i in range(1, rows):
		for j in range(1, cols):
			# compute the ways through dynamic progress
			grid[i][j] = grid[i-1][j] + grid[i][j-1]

	return grid[rows-1][cols-1]	

if __name__ == "__main__":
	print(lattice_paths(3, 3))
	print(lattice_paths(21, 21))
