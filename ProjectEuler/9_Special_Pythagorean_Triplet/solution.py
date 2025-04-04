def special_pythagorean_triplet(target):
    """
    Question: A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2.
    For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2
    There exists exactly one Pythagorean triplet for which a + b + c = 1000.Find the product abc.
	Optimation: from the condition -> a < b < c, we can infer that a <= target/3 and b < (target-a)/2.
    """
    for a in range(1, target):  # a must be less than target/3
        for b in range(a + 1, (target - a)):  # b must be greater than a and less than (target - a)/2
            c = target - a - b
            if a**2 + b**2 == c**2:
                return a * b * c
    return None

if __name__ == "__main__":
    print(special_pythagorean_triplet(12))  # Test with a smaller target
    print(special_pythagorean_triplet(1000))  # Actual problem
