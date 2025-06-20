"""
给定一个二进制数组 nums ， 计算其中最大连续 1 的个数。
"""

from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = 0
        slow = 0

        for fast in range(len(nums)):
            if nums[fast] == 0:
                maxCount = max(maxCount, fast - slow)
                slow = fast + 1  # 跳过 0，开始新的连续子数组

        # 需要考虑数组最后的连续 1
        return max(maxCount, fast - slow + 1)
    
def test():
    sol = Solution()
    test_cases = [
        ([1, 1, 0, 1, 1, 1], 3),  # 连续 1 的最大子数组长度是 3
        ([1, 0, 1, 1, 0, 1], 2),  # 连续 1 的最大子数组长度是 2
        ([0, 0, 0, 0], 0),  # 没有 1，返回 0
        ([1, 1, 1, 1], 4),  # 全是 1，返回 4
        ([1, 0, 1, 0, 1, 0, 1], 1),  # 每个 1 都单独出现，返回 1
    ]
    
    for i, (nums, expected) in enumerate(test_cases, 1):
        result = sol.findMaxConsecutiveOnes(nums)
        print(f"Test case {i}:")
        print(f"Input: {nums}")
        print(f"Expected: {expected}, Result: {result}")
        print("✅ Pass" if result == expected else "❌ Fail")
        print("-" * 40)

if __name__ == "__main__":
    test()
