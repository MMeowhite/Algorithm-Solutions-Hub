"""
给你一幅由 N × N 矩阵表示的图像，其中每个像素的大小为 4 字节。请你设计一种算法，将图像旋转 90 度。
不占用额外内存空间能否做到？
"""


from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # matrix[:]=zip(*matrix[::-1]) return type: List[tuple]
        # matrix[:] = [list(row) for row in zip(*matrix[::-1])] return type: List[List[int]]
        n = len(matrix)

        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in matrix:
            row.reverse()
                 

def test():
    sol = Solution()

    test_cases = [
        (
            [[1, 2], [3, 4]],
            [[3, 1], [4, 2]]
        ),
        (
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        ),
        (
            [[1]],
            [[1]]
        ),
        (
            [[5, 1, 9, 11],
             [2, 4, 8, 10],
             [13, 3, 6, 7],
             [15, 14, 12, 16]],
            [[15, 13, 2, 5],
             [14, 3, 4, 1],
             [12, 6, 8, 9],
             [16, 7, 10, 11]]
        )
    ]

    for i, (input_matrix, expected) in enumerate(test_cases, 1):
        matrix = [row[:] for row in input_matrix]  # 深拷贝，避免修改原始数据
        sol.rotate(matrix)
        print(f"Test case {i}:")
        print(f"Input:    {input_matrix}")
        print(f"Expected: {expected}")
        print(f"Result:   {matrix}")
        if matrix == expected:
            print("✅ Pass")
        else:
            print("❌ Fail")
        print("-" * 50)

if __name__ == "__main__":
    test()
    