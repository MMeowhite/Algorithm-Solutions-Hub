"""
在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。
"""

from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]
        max_len = 0

        for i in range(rows):
            for j in range(cols):
                # 判断以位置 (i, j) 为右下角的最大正方形的边长是多少
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(
                            dp[i - 1][j],
                            dp[i][j - 1],
                            dp[i - 1][j - 1]
                        ) + 1
                    max_len = max(max_len, dp[i][j])

        return max_len * max_len

def test():
    solution = Solution()
    test_cases = [
        (
            [
                ["1", "0", "1", "0", "0"],
                ["1", "0", "1", "1", "1"],
                ["1", "1", "1", "1", "1"],
                ["1", "0", "0", "1", "0"]
            ],
            4
        ),
        (
            [
                ["0", "1"],
                ["1", "0"]
            ],
            1
        ),
        (
            [
                ["0"]
            ],
            0
        ),
        (
            [
                ["1"]
            ],
            1
        ),
        (
            [
                ["1", "1"],
                ["1", "1"]
            ],
            4
        ),
        (
            [
                ["0", "0", "0"],
                ["0", "0", "0"],
                ["0", "0", "0"]
            ],
            0
        ),
        (
            [],
            0
        )
    ]

    for i, (matrix, expected) in enumerate(test_cases, 1):
        result = solution.maximalSquare(matrix)
        print(f"Test case {i}:")
        print(f"Expected: {expected}, Got: {result}", end=" ")
        print("✅ Pass" if result == expected else "❌ Fail")
        print("-" * 40)


if __name__ == "__main__":
    test()