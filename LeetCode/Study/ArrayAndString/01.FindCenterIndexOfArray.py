"""
给你一个整数数组:nums ，请计算数组的 中心下标 。
数组 中心下标 是数组的一个下标，其左侧所有元素相加的和等于右侧所有元素相加的和。
如果中心下标位于数组最左端，那么左侧数之和视为 0 ，因为在下标的左侧不存在元素。这一点对于中心下标位于数组最右端同样适用。
如果数组有多个中心下标，应该返回 最靠近左边 的那一个。如果数组不存在中心下标，返回 -1 。
"""

from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = sum(nums)
        left_sum = 0

        for i, num in enumerate(nums):
            if left_sum == total_sum - left_sum - num:
                return i
            left_sum += num

        return -1

def test():
    sol = Solution()
    
    test_cases = [
        ([1, 7, 3, 6, 5, 6], 3),
        ([1, 2, 3], -1),
        ([2, 1, -1], 0),
        ([0, 0, 0, 0], 0),
        ([1], 0),
        ([1, -1, 0], 2)
    ]
    
    for i, (nums, expected) in enumerate(test_cases):
        result = sol.pivotIndex(nums)
        print(f"Test case {i+1}: nums = {nums}")
        print(f"Expected: {expected}, Got: {result}")
        print("Pass ✅" if result == expected else "Fail ❌")
        print("-" * 40)


if __name__ == "__main__":
    test()