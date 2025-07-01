"""
T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2
给你整数 n，请返回第 n 个泰波那契数 Tn 的值。
"""

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        
        a, b, c = 0, 1, 1
        for _ in range(3, n+1):
            temp = a + b + c
            a = b
            b = c
            c = temp

        return c
    
def test():
    sol = Solution()
    test_cases = [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 4),
        (5, 7),
        (10, 149),
        (20, 66012),
    ]

    for i, (n, expected) in enumerate(test_cases):
        result = sol.tribonacci(n)
        print(f"Test case {i+1}: tribonacci({n})")
        print(f"Expected: {expected}, Got: {result}")
        print("✅ Pass" if result == expected else "❌ Fail")
        print("-" * 30)

if __name__ == "__main__":
    test()
