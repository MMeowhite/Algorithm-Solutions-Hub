"""
给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。
在「杨辉三角」中，每个数是它左上方和右上方的数的和。
"""
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            triangle.append(row)

        return triangle
    
def test():
    sol = Solution()
    test_cases = [
        (0, []),  # 0 行
        (1, [[1]]),  # 1 行
        (2, [[1], [1, 1]]),  # 2 行
        (3, [[1], [1, 1], [1, 2, 1]]),  # 3 行
        (4, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]),  # 4 行
        (5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]),  # 5 行
    ]
    
    for i, (numRows, expected) in enumerate(test_cases):
        result = sol.generate(numRows)
        print(f"Test case {i + 1}:")
        print(f"Input: {numRows}")
        print(f"Expected: {expected}, Result: {result}")
        print("✅ Pass" if result == expected else "❌ Fail")
        print("-" * 40)

if __name__ == "__main__":
    test()