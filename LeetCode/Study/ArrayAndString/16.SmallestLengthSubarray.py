"""
给定一个含有 n 个正整数的数组和一个正整数 target 。
找出该数组中满足其总和大于等于 target 的长度最小的 子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。
"""

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        min_length = float('inf')  # 初始化最小长度为无穷大
        current_sum = 0  # 当前窗口的和
        left = 0  # 滑动窗口的左边界

        # 遍历数组，右边界逐步扩大
        for right in range(n):
            current_sum += nums[right]  # 扩大窗口，累加右边界的元素

            # 当窗口和大于等于目标值时，尝试缩小窗口
            while current_sum >= target:
                # 更新最小长度
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]  # 缩小窗口，移动左边界
                left += 1  # 移动左边界，减少窗口和

        # 如果找到了满足条件的子数组，返回最小长度，否则返回 0
        return min_length if min_length != float('inf') else 0


def test():
    sol = Solution()
    test_cases = [
        (7, [2, 3, 1, 2, 4, 3], 2),  # 最小子数组长度是 2, 子数组是 [4, 3]
        (4, [1, 4, 4], 1),  # 最小子数组长度是 1, 子数组是 [4]
        (11, [1, 1, 1, 1, 1, 1, 1, 1], 0),  # 没有满足条件的子数组
        (15, [1, 2, 3, 4, 5], 5),  # 最小子数组长度是 5, 子数组是 [1, 2, 3, 4, 5]
        (8, [1, 1, 1, 1, 1, 1, 1, 1], 8),  # 最小子数组长度是 8, 子数组是整个数组
    ]
    
    for i, (target, nums, expected) in enumerate(test_cases, 1):
        result = sol.minSubArrayLen(target, nums)
        print(f"Test case {i}:")
        print(f"Target: {target}, Nums: {nums}")
        print(f"Expected: {expected}, Result: {result}")
        print("✅ Pass" if result == expected else "❌ Fail")
        print("-" * 40)

if __name__ == "__main__":
    test()
