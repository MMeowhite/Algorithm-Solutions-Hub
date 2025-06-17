"""
编写一种算法，若M × N矩阵中某个元素为0，则将其所在的行与列清零。
"""
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        if m == 0:
            return 
        n = len(matrix[0])

        rows = set()
        cols = set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)


        for i in rows:
            for j in range(n):
                matrix[i][j] = 0
        
        for j in cols:
            for i in range(m):
                matrix[i][j] = 0

def test():
    sol = Solution()

    test_cases = [
        (
            [[1, 1, 1], [1, 0, 1], [1, 1, 1]],
            [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
        ),
        (
            [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]],
            [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
        ),
        (
            [[1]],
            [[1]]
        ),
        (
            [[0]],
            [[0]]
        ),
        (
            [],
            []
        )
    ]

    for i, (matrix, expected) in enumerate(test_cases, 1):
        sol.setZeroes(matrix)
        print(f"Test case {i}:")
        print(f"Result:   {matrix}")
        print(f"Expected: {expected}")
        if matrix == expected:
            print("✅ Pass")
        else:
            print("❌ Fail")
        print("-" * 30)


if __name__ == "__main__":
    test()