def permutations(iterable):
    # 如果可迭代对象的长度为1，则只有一种排列
    if len(iterable) == 1:
        return [iterable]
    # 递归生成所有排列
    result = []
    for i in range(len(iterable)):
        # 选择一个元素作为排列的开头
        current = iterable[i]
        # 对剩下的元素生成排列
        remaining = iterable[:i] + iterable[i+1:]
        for perm in permutations(remaining):
            # 将开头的元素与后面的排列组合起来
            result.append(current + perm)
    return result

def substring_divisibility():
    """
    Question: The number, 1406357289 is a 0 to 9 pandigital number because it
    is made up of each the digits 0 to 9 in some order, but it also has a rather
    interesting sub-stirng divisibility property
    Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we
    note that the following:
        d2d3d4 = 406 is divisible by 2
        d3d4d5 = 063 is divisible by 3
        d4d5d6 = 635 is divisible by 5
        d5d6d7 = 357 is divisible by 7
        d6d7d8 = 572 is divisible by 11
        d7d8d9 = 728 is divisible by 13
        d8d9d10 = 289 is divisible by 17
    Find the sum of all 0 to 9 pandigital numbers with this property.
    """
    # Generate all permutations of the digits 0 to 9
    pandigital_numbers = permutations('0123456789')

    # Define the divisors for each substring
    divisors = [2, 3, 5, 7, 11, 13, 17]

    # Filter the pandigital numbers that satisfy the substring divisibility property
    valid_numbers = []
    for num in pandigital_numbers:
        num_str = num
        if num_str[0] == '0':  # Skip numbers starting with '0'
            continue

        # Check d2d3d4 is divisible by 2
        if int(num_str[1:4]) % 2 != 0:
            continue

        # Check d3d4d5 is divisible by 3
        if int(num_str[2:5]) % 3 != 0:
            continue

        # Check d4d5d6 is divisible by 5
        if int(num_str[3:6]) % 5 != 0:
            continue

        # Check d5d6d7 is divisible by 7
        if int(num_str[4:7]) % 7 != 0:
            continue

        # Check d6d7d8 is divisible by 11
        if int(num_str[5:8]) % 11 != 0:
            continue

        # Check d7d8d9 is divisible by 13
        if int(num_str[6:9]) % 13 != 0:
            continue

        # Check d8d9d10 is divisible by 17
        if int(num_str[7:10]) % 17 != 0:
            continue

        valid_numbers.append(int(num_str))

    # Return the sum of the valid pandigital numbers
    return sum(valid_numbers)

if __name__ == "__main__":
    print(substring_divisibility())
