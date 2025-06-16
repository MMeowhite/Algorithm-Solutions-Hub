"""
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi]
请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间
"""
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        # 步骤 1: 按 start 排序
        intervals.sort(key=lambda x: x[0])
        merged = []

        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                # 无重叠，直接加入
                merged.append(interval)
            else:
                # 有重叠，合并区间
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
    
def test():
    sol = Solution()

    test_cases = [
        ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
        ([[1, 4], [4, 5]], [[1, 5]]),
        ([[1, 4], [0, 2], [3, 5]], [[0, 5]]),
        ([[1, 4]], [[1, 4]]),
        ([], [])
    ]

    for i, (intervals, expected) in enumerate(test_cases, 1):
        result = sol.merge(intervals)
        print(f"Test case {i}:")
        print(f"Input:    {intervals}")
        print(f"Expected: {expected}")
        print(f"Result:   {result}")
        if result == expected:
            print("✅ Pass")
        else:
            print("❌ Fail")
        print("-" * 50)

if __name__ == "__main__":
    test()