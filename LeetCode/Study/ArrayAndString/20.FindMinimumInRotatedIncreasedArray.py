"""
已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转 后，得到输入数组。例如，原数组 nums = [0,1,2,4,5,6,7] 在变化后可能得到：
若旋转 4 次，则可以得到 [4,5,6,7,0,1,2]
若旋转 7 次，则可以得到 [0,1,2,4,5,6,7]
注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], ..., a[n-2]] 。
给你一个元素值 互不相同 的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。
你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。
"""

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            
            # 如果中间元素大于右边界元素，说明最小值在右半部分
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # 否则最小值在左半部分或中间元素就是最小值
                right = mid

        # 当 left == right 时，left 或 right 都指向最小值
        return nums[left]
    
def test():
    sol = Solution()
    test_cases = [
        ([3, 4, 5, 1, 2], 1),  # 最小值是 1
        ([4, 5, 6, 7, 0, 1, 2], 0),  # 最小值是 0
        ([11, 13, 15, 17], 11),  # 没有旋转，最小值是第一个元素
        ([2, 3, 4, 5, 6, 7, 8], 2),  # 没有旋转，最小值是第一个元素
        ([1], 1),  # 单个元素数组，最小值就是它本身
    ]
    
    for i, (nums, expected) in enumerate(test_cases, 1):
        result = sol.findMin(nums)
        print(f"Test case {i}:")
        print(f"Input: {nums}")
        print(f"Expected: {expected}, Result: {result}")
        print("✅ Pass" if result == expected else "❌ Fail")
        print("-" * 40)

if __name__ == "__main__":
    test()