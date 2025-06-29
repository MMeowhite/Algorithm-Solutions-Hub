"""
给你一个非负整数 num ，请你返回将它变成 0 所需要的步数。 如果当前数字是偶数，你需要把它除以 2 ；否则，减去 1 。
"""

class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        
        while num > 0:
            if num % 2 == 0:
                num = num // 2
            else:
                num -= 1
            count += 1
        
        return count
    
def test():
    sol = Solution()

    test_cases = [
        (14, 6),
        (8, 4),
        (123, 12),
        (0, 0),
        (1, 1)
    ]

    for i, (num, expected) in enumerate(test_cases):
        result = sol.numberOfSteps(num)
        print(f"Test case {i+1}: num = {num}")
        print(f"Expected: {expected}, Got: {result}")
        print("Pass ✅" if result == expected else "Fail ❌")
        print("-" * 40)

if __name__ == "__main__":
    test()