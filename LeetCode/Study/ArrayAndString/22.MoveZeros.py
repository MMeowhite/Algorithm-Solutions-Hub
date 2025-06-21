"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
请注意 ，必须在不复制数组的情况下原地对数组进行操作。
"""

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_non_zero = 0
        
        # 将非零元素移动到数组的前面
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_non_zero] = nums[i]
                last_non_zero += 1

        # 将剩余的元素设置为 0
        for i in range(last_non_zero, len(nums)):
            nums[i] = 0

def test():
    sol = Solution()
    test_cases = [
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),  # 移动 0 到末尾
        ([0, 0, 1], [1, 0, 0]),  # 多个连续的 0
        ([1, 2, 3], [1, 2, 3]),  # 没有 0
        ([0], [0]),  # 单个元素是 0
        ([1], [1]),  # 单个非零元素
    ]
    
    for i, (nums, expected) in enumerate(test_cases, 1):
        sol.moveZeroes(nums)
        print(f"Test case {i}:")
        print(f"Input: {nums}")
        print(f"Expected: {expected}, Result: {nums}")
        print("✅ Pass" if nums == expected else "❌ Fail")
        print("-" * 40)

if __name__ == "__main__":
    test()