"""
给定一个非负索引 rowIndex，返回「杨辉三角」的第 rowIndex 行。
在「杨辉三角」中，每个数是它左上方和右上方的数的和。
"""

from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for i in range(1, rowIndex + 1):
            # 逆序更新，避免覆盖
            for j in range(i - 1, 0, -1):
                row[j] = row[j] + row[j - 1]
            row.append(1)
        return row

def test():
    sol = Solution()
    test_cases = [
        (0, [1]),  # 第 0 行
        (1, [1, 1]),  # 第 1 行
        (2, [1, 2, 1]),  # 第 2 行
        (3, [1, 3, 3, 1]),  # 第 3 行
        (4, [1, 4, 6, 4, 1]),  # 第 4 行
        (5, [1, 5, 10, 10, 5, 1]),  # 第 5 行
    ]
    
    for i, (rowIndex, expected) in enumerate(test_cases):
        result = sol.getRow(rowIndex)
        print(f"Test case {i + 1}:")
        print(f"Input: {rowIndex}")
        print(f"Expected: {expected}, Result: {result}")
        print("✅ Pass" if result == expected else "❌ Fail")
        print("-" * 40)

if __name__ == "__main__":
    test()