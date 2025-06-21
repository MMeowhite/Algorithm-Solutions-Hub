"""
给你一个 非严格递增排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。元素的 相对顺序 应该保持 一致 。然后返回 nums 中唯一元素的个数。
考虑 nums 的唯一元素的数量为 k ，你需要做以下事情确保你的题解可以被通过：
更改数组 nums ，使 nums 的前 k 个元素包含唯一元素，并按照它们最初在 nums 中出现的顺序排列。nums 的其余元素与 nums 的大小不重要。
返回 k 。
"""


from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1
    
def test():
    sol = Solution()
    test_cases = [
        ([1, 1, 2], 2),  # 删除重复元素后，数组变为 [1, 2]
        ([0, 0, 1, 1, 1, 2, 2, 3], 4),  # 删除重复元素后，数组变为 [0, 1, 2, 3]
        ([1], 1),  # 单个元素，返回长度为 1
        ([], 0),  # 空数组，返回长度为 0
        ([1, 2, 3], 3),  # 没有重复元素，返回长度为原数组长度
    ]
    
    for i, (nums, expected) in enumerate(test_cases, 1):
        result = sol.removeDuplicates(nums)
        print(f"Test case {i}:")
        print(f"Input: {nums}")
        print(f"Expected: {expected}, Result: {result}")
        print("✅ Pass" if result == expected else "❌ Fail")
        print("-" * 40)

if __name__ == "__main__":
    test()