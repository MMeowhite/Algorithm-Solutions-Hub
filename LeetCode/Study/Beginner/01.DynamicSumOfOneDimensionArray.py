"""
给你一个数组 nums 。数组「动态和」的计算公式为：runningSum[i] = sum(nums[0]…nums[i]) 。
请返回 nums 的动态和。
"""

from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        dynamic_sum = []
        current_sum = 0

        for i in range(len(nums)):
            current_sum += nums[i]
            dynamic_sum.append(current_sum)
        
        return dynamic_sum
        # n = len(nums)
        # for i in range(1, n):
        #     nums[i] += nums[i - 1]
        # return nums

def test():
    sol = Solution()

    test_cases = [
        ([1, 2, 3, 4], [1, 3, 6, 10]),
        ([1, 1, 1, 1, 1], [1, 2, 3, 4, 5]),
        ([3, 1, 2, 10, 1], [3, 4, 6, 16, 17]),
        ([], []),
        ([5], [5])
    ]

    for i, (nums, expected) in enumerate(test_cases):
        result = sol.runningSum(nums)
        print(f"Test case {i+1}: nums = {nums}")
        print(f"Expected: {expected}, Got: {result}")
        print("Pass ✅" if result == expected else "Fail ❌")
        print("-" * 40)

if __name__ == "__main__":
    test()


    
