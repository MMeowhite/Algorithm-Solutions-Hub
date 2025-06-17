"""
给你一个大小为 m x n 的矩阵 mat ，请以对角线遍历的顺序，用一个数组返回这个矩阵中的所有元素。
"""

from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []

        m, n = len(mat), len(mat[0])
        result = []

        for s in range(m + n - 1): # s为对角线的范围
            # 存当前对角线的元素
            intermediate = []
            
            # i 范围：[max(0, s - n + 1), min(s, m - 1)]
            start_row = max(0, s - n + 1)
            end_row = min(s, m - 1)
            for i in range(start_row, end_row + 1):
                # i,j 是当前对角线上的元素坐标
                j = s - i
                intermediate.append(mat[i][j])
            
            # 偶数条对角线反转，奇数条保持
            if s % 2 == 0:
                intermediate.reverse()
            
            result.extend(intermediate)
        
        return result
    
def test():
    sol = Solution()

    test_cases = [
        (
            [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]],
            [1, 2, 4, 7, 5, 3, 6, 8, 9]
        ),
        (
            [[1, 2],
             [3, 4]],
            [1, 2, 3, 4]
        ),
        (
            [[1]],
            [1]
        ),
        (
            [[]],
            []
        ),
        (
            [],
            []
        )
    ]

    for i, (matrix, expected) in enumerate(test_cases, 1):
        result = sol.findDiagonalOrder(matrix)
        print(f"Test case {i}:")
        print(f"Input:    {matrix}")
        print(f"Expected: {expected}")
        print(f"Result:   {result}")
        print("✅ Pass" if result == expected else "❌ Fail")
        print("-" * 40)


if __name__ == "__main__":
    test()