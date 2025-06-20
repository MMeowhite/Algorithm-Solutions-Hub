"""
给定长度为 2n 的整数数组 nums ，你的任务是将这些数分成 n 对, 例如 (a1, b1), (a2, b2), ..., (an, bn) ，使得从 1 到 n 的 min(ai, bi) 总和最大。
返回该 最大总和 。
"""

from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])
        # return sum(sorted(nums)[::2])


def test():
    sol = Solution()
    test_cases = [
        ([1, 4, 3, 2], 4),          # pairs: (1,2), (3,4) -> sum = 1 + 3 = 4
        ([6, 2, 6, 5, 1, 2], 9),    # pairs: (1,2), (2,5), (6,6) -> sum = 1+2+6=9
        ([1, 1], 1),                # (1,1) -> sum = 1
        ([1, 2, 3, 4, 5, 6], 9),    # (1,2), (3,4), (5,6) -> sum = 1+3+5=9
        ([-1, 0, 1, 2], 0),         # (-1,0), (1,2) -> sum = -1+1 = 0
        ([7, 3], 3),                # (3,7) -> sum = 3
        ([100, 200, 300, 400], 400) # (100,200), (300,400) -> sum = 100+300=400
    ]

    for i, (nums, expected) in enumerate(test_cases, 1):
        result = sol.arrayPairSum(nums)
        print(f"Test case {i}:")
        print(f"Input: {nums}")
        print(f"Expected: {expected}, Result: {result}")
        print("✅ Pass" if result == expected else "❌ Fail")
        print("-" * 40)

if __name__ == "__main__":
    test()