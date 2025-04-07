import math

def highly_divisible_triangular_number(divisors_number):
    """ 
	Question: The sequence of triangle numbers is generated by adding the
	natural numbers. So the 7th triangle number would be 1+2+3+4+5+6+7=28.
	The first ten terms would be: 1,3,6,10,15,21,28,36,45,55
	Let us list the factors of the first seven triangle numbers:
		1:1
		3:1,3
		6,1,2,3,6
		10:1,2,5,10
		15:1,3,5,10
		21:1,3,7,21
		28:1,2,4,7,14,28
    """
    number = 1
    while True:
        triangular_number = generate_accumulated_sum(number)
        divisors = compute_divisor_number(triangular_number)
        if divisors > divisors_number:
            return triangular_number
        number += 1

def generate_accumulated_sum(index):
    return index * (index + 1) // 2

def compute_divisor_number(number):
    if number == 1:
        return 1
    count = 0
    sqrt_n = int(math.sqrt(number))
    for i in range(1, sqrt_n + 1):
        if number % i == 0:
            if i * i == number:
                count += 1
            else:
                count += 2
    return count

if __name__ == "__main__":
    print(generate_accumulated_sum(7))  
    print(compute_divisor_number(28))  
    print(highly_divisible_triangular_number(5)) 
    print(highly_divisible_triangular_number(500))
