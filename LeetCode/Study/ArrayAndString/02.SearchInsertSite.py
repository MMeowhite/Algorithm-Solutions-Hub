"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
请必须使用时间复杂度为 O(log n) 的算法。
"""

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        return start
    
def test():
    sol = Solution()
    test_cases = [
        ([1, 3, 5, 6], 5, 2),
        ([1, 3, 5, 6], 2, 1),
        ([1, 3, 5, 6], 7, 4),
        ([1, 3, 5, 6], 0, 0),
        ([1], 0, 0),
        ([1], 1, 0),
        ([1], 2, 1),
    ]

    for i, (nums, target, expected) in enumerate(test_cases):
        result = sol.searchInsert(nums, target)
        print(f"Test case {i+1}: nums = {nums}, target = {target}")
        print(f"Expected: {expected}, Got: {result}")
        print("✅ Pass" if result == expected else "❌ Fail")
        print("-" * 40)


if __name__ == "__main__":
    test()   