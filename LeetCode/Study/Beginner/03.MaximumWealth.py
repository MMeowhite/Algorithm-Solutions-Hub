"""
给你一个 m x n 的整数网格 accounts ，其中 accounts[i][j] 是第 i​​​​​​​​​​​​ 位客户在第 j 家银行托管的资产数量。返回最富有客户所拥有的 资产总量 。
客户的 资产总量 就是他们在各家银行托管的资产数量之和。最富有客户就是 资产总量 最大的客户。
"""

from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maximum_wealth = 0

        for i in range(len(accounts)):
            wealth = 0
            for j in range(len(accounts[0])):
                wealth += accounts[i][j]
            
            if maximum_wealth < wealth:
                maximum_wealth = wealth
        
        return maximum_wealth
    
def test():
    sol = Solution()

    test_cases = [
        ([[1, 2, 3], [3, 2, 1]], 6),
        ([[1, 5], [7, 3], [3, 5]], 10),
        ([[2, 8, 7], [7, 1, 3], [1, 9, 5]], 17),
        ([[0, 0, 0]], 0),
        ([[]], 0),
        ([[100]], 100)
    ]

    for i, (accounts, expected) in enumerate(test_cases):
        result = sol.maximumWealth(accounts)
        print(f"Test case {i+1}: accounts = {accounts}")
        print(f"Expected: {expected}, Got: {result}")
        print("Pass ✅" if result == expected else "Fail ❌")
        print("-" * 40)

if __name__ == "__main__":
    test()