import string

def names_scores(file_path):
	"""
	Question: Using names.txt. which contains over five-thousand first names,
	begin by sorting it into alphabetical order. Then working out the
	alphabetical value for each name, multiply this value by its alphabetical
	position in the list to obtain a name score
	For example, when the list is sorted into alphabetical order, COLIN, which
	is worth 3+15+12+9+14=53, is the 938th name in the list. So, COLIN would
	obtain a score 938x53=49714
	What is the total of all the name scores in the file?
	"""

	alphabetical_table = {}
	for index, char in enumerate(string.ascii_lowercase, start=1):
		alphabetical_table[char] = index
	
	names = read_and_preprocess(file_path)
	names.sort()
	total = 0
	for index, name in enumerate(names, start=1):
		char_sum = 0
		for char in name.lower():
			char_sum += alphabetical_table.get(char, 0)
		total += char_sum * index
	
	return total
		

def read_and_preprocess(file_path):
	"""
	read and preprocess a .txt file
	"""
	try:
		with open(file_path, 'r') as file:
			lines = file.readlines() # read all lines in a file
			result = []
			for line in lines:
				elements = line.strip().split(',')
				elemnets = [element.strip() for element in elements if element.strip()]
				result.extend(elements)
			return result
	except FileNotFoundError:
		raise FileNotFoundError("file is not exists")
		return []
	except Exception as e:
		raise Exception("a fatal error in reading file")
		return []

if __name__ == "__main__":
# result = read_and_preprocess("names.txt")
# print(result)
	print(names_scores("names.txt"))
