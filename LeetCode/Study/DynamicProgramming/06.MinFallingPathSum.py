"""
给你一个 n x n 的 方形 整数数组 matrix ，请你找出并返回通过 matrix 的下降路径 的 最小和 。
下降路径 可以从第一行中的任何元素开始，并从每一行中选择一个元素。
在下一行选择的元素和当前行所选元素最多相隔一列（即位于正下方或者沿对角线向左或者向右的第一个元素）。
具体来说，位置 (row, col) 的下一个元素应当是 (row + 1, col - 1)、(row + 1, col) 或者 (row + 1, col + 1) 。
"""

from typing import List

class Solution:
    # 1. 原地修改 matrix（空间 O(1)）
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        for i in range(n - 2, -1, -1):
            for j in range(n):
                left = matrix[i + 1][j - 1] if j > 0 else float('inf')
                mid = matrix[i + 1][j]
                right = matrix[i + 1][j + 1] if j < n - 1 else float('inf')
                matrix[i][j] += min(left, mid, right)
        return min(matrix[0])

    # 2. 使用额外的二维 dp 数组（空间 O(n^2)）
    def minFallingPathSumOptim(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[0] * n for _ in range(n)]

        # 初始化最后一行
        dp[-1] = matrix[-1][:]

        for i in range(n - 2, -1, -1):
            for j in range(n):
                left = dp[i + 1][j - 1] if j > 0 else float('inf')
                mid = dp[i + 1][j]
                right = dp[i + 1][j + 1] if j < n - 1 else float('inf')
                dp[i][j] = matrix[i][j] + min(left, mid, right)

        return min(dp[0])

    # 3. 使用两个一维数组进行滚动（空间 O(n)）
    def minFallingPathSumOptimOptim(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        prev = matrix[-1][:]  # 初始化为最后一行

        for i in range(n - 2, -1, -1):
            curr = [0] * n
            for j in range(n):
                left = prev[j - 1] if j > 0 else float('inf')
                mid = prev[j]
                right = prev[j + 1] if j < n - 1 else float('inf')
                curr[j] = matrix[i][j] + min(left, mid, right)
            prev = curr

        return min(prev)
        
def test():
    solution = Solution()
    test_cases = [
        (
            [
                [2, 1, 3],
                [6, 5, 4],
                [7, 8, 9]
            ],
            13
        ),
        (
            [
                [-19, 57],
                [-40, -5]
            ],
            -59
        ),
        (
            [
                [100]
            ],
            100
        ),
        (
            [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
            ],
            12
        )
    ]

    methods = [
        solution.minFallingPathSum,
        solution.minFallingPathSumOptim,
        solution.minFallingPathSumOptimOptim
    ]

    for method in methods:
        print(f"Testing method: {method.__name__}")
        for i, (matrix, expected) in enumerate(test_cases, 1):
            try:
                # 深拷贝 matrix 防止原地修改影响下一个 case
                import copy
                result = method(copy.deepcopy(matrix))
                print(f"Test case {i}:")
                print(f"Input: {matrix}")
                print(f"Expected: {expected}, Got: {result}", end=" ")
                print("✅ Pass" if result == expected else "❌ Fail")
            except Exception as e:
                print(f"Test case {i} raised an exception: {e} ❌")
            print("-" * 50)
        print("=" * 60)

if __name__ == "__main__":
    test()
