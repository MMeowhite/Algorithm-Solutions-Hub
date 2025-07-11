"""
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
"""

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        prev2 = nums[0]
        prev1 = max(nums[0], nums[1]);

        for i in range(2, n):
            cur = max(prev1, prev2 + nums[i])
            prev2 = prev1
            prev1 = cur
        
        return prev1

def test():
    solution = Solution()
    test_cases = [
        ([1, 2, 3, 1], 4),          
        ([2, 7, 9, 3, 1], 12),      
        ([2, 1, 1, 2], 4),          
        ([5, 5, 10, 100, 10, 5], 110), 
        ([1], 1),                   
        ([0], 0),                   
        ([1, 2], 2),                
        ([2, 1], 2),                
        ([], 0),                    
        ([4, 1, 2, 9, 1], 13),    
    ]

    for i, (nums, expected) in enumerate(test_cases, 1):
        result = solution.rob(nums)
        print(f"Test case {i}: nums = {nums}")
        print(f"Expected: {expected}, Got: {result}", end=" ")
        print("✅ Pass" if result == expected else "❌ Fail")
        print("-" * 40)

if __name__ == "__main__":
    test()