def number_spiral_diagonals(rows, cols):
	"""
	Question: Starting with number 1 and moving to the right
	"""
	
	matrix = generate_spiral_matrix(rows, cols)
	total = 0
	# method 1
	# for i in range(rows):
	#	total += 2 * matrix[i][cols // 2]
	
	# return (total - 1)
	# method 2
	total = 1
	for k in range(1, (rows + 1) //2):
		layer_sum = 4 * (2 * k + 1) ** 2 - 6 * (2 * k)
		total += layer_sum

	return total



def generate_spiral_matrix(rows, cols):
	"""
	Generating the spiral matrix
	"""
	if rows != cols:
		raise ValueError("rows must be equal to cols!")
	if rows % 2 == 0:
		raise ValueError("rows and cols must be an odd integer number!")

	directions = [(0,1), (1,0),(0,-1),(-1, 0)] # right, down, left, up for each turple
	direction_idx = 0

	matrix = [[0 for _ in range(cols)] for _ in range(rows)]
	row, col = rows // 2, cols // 2
	matrix[row][col] = 1
	
	num = 2 # fill the matrix from 2
	steps = 1
	max_steps = rows * cols

	while num <= max_steps:
		for _ in range(steps):
			if num > max_steps:
				break
			# move to next direction
			row += directions[direction_idx][0]
			col += directions[direction_idx][1]
			matrix[row][col] = num
			num += 1
		# change drection
		direction_idx = (direction_idx + 1) % 4

		# every two direction, step plus 1
		if direction_idx % 2 == 0:
			steps += 1

	return matrix

if __name__ == "__main__":
	print(generate_spiral_matrix(5,5))
	print(number_spiral_diagonals(1001, 1001))
