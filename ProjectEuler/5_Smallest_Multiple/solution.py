def smallest_multiple(target):
    """
    Question: 2520 is the smallest number that can be divided by each of the
    numbers from 1 to 10 without any remainder. What is the smallest
    positive number that is evenly divisible by all of the numbers from 1 to
    20?
    """
    result = 1

    for i in range(1, target + 1):
        result = (result * i) // gcd(result, i)
    return result

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

if __name__ == "__main__":
    print(smallest_multiple(10))
    print(smallest_multiple(20))
