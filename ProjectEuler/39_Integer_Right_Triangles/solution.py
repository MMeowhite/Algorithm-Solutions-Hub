def integer_right_triangles(p):
	"""
	Question:If p is the perimeter of a right angle triangle with integral
	length sides, {a,b,c}, there are exactly three solution for p = 120.
{20,48,52},{24,45,51},{30,40,50}
	For which value of p <= 1000, is the number of solutions maxmised?
	"""
	max_solutions = 0
	current_p = 0
	for perimeter in range(p+1):
		solutions = 0
		for a in range(1, perimeter // 3 + 1):
			for b in range(a, (perimeter - a)//2 + 1):
				c = perimeter - a - b
				if a**2 + b**2 == c**2:
					solutions += 1

		if max_solutions < solutions:
			max_solutions = solutions
			current_p = perimeter

	return current_p



if __name__ == "__main__":
	print(integer_right_triangles(1000))
