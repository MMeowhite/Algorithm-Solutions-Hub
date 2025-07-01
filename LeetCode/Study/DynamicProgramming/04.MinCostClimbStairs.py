"""
给你一个整数数组 cost ，其中 cost[i] 是从楼梯第 i 个台阶向上爬需要支付的费用。一旦你支付此费用，即可选择向上爬一个或者两个台阶。
你可以选择从下标为 0 或下标为 1 的台阶开始爬楼梯。
请你计算并返回达到楼梯顶部的最低花费。
"""

from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a, b = cost[0], cost[1]
        for i in range(2, len(cost)):
            a, b = b, cost[i] + min(a, b)
        return min(a, b)

        # n = len(cost)
        # dp = [0] * n
        
        # dp[0] = cost[0]
        # dp[1] = cost[1]

        # for i in range(2, n):
        #     dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
        
        # return min(dp[-1], dp[-2])
    
def test():
    sol = Solution()
    test_cases = [
        ([10, 15, 20], 25),        
        ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 104), 
        ([0, 0, 0, 0], 0),          
        ([1, 2], 1),                
        ([1, 2, 3], 2),             
        ([10, 5, 2, 1, 4], 6),     
    ]

    for i, (cost, expected) in enumerate(test_cases, 1):
        result = sol.minCostClimbingStairs(cost)
        print(f"Test case {i}: cost = {cost}")
        print(f"Expected: {expected}, Got: {result}")
        print("✅ Pass" if result == expected else "❌ Fail")
        print("-" * 30)

if __name__ == "__main__":
    test()