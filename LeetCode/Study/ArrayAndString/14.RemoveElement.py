"""
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素。元素的顺序可能发生改变。然后返回 nums 中与 val 不同的元素的数量。
假设 nums 中不等于 val 的元素数量为 k，要通过此题，您需要执行以下操作：
更改 nums 数组，使 nums 的前 k 个元素包含不等于 val 的元素。nums 的其余元素和 nums 的大小并不重要。
返回 k。
用户评测：

评测机将使用以下代码测试您的解决方案：

int[] nums = [...]; // 输入数组
int val = ...; // 要移除的值
int[] expectedNums = [...]; // 长度正确的预期答案。
                            // 它以不等于 val 的值排序。

int k = removeElement(nums, val); // 调用你的实现

assert k == expectedNums.length;
sort(nums, 0, k); // 排序 nums 的前 k 个元素
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
如果所有的断言都通过，你的解决方案将会 通过。
"""

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]  # 将符合条件的元素移到前面
                slow += 1  # 增加有效元素的个数

        return slow  # 返回有效元素的个数
    
def test():
    sol = Solution()
    test_cases = [
        ([3, 2, 2, 3], 3, 2),  # 删除 3 后，剩下 [2, 2]
        ([0, 1, 2, 2, 3, 0, 4, 2], 2, 5),  # 删除 2 后，剩下 [0, 1, 3, 0, 4]
        ([1, 1, 1, 1], 1, 0),  # 删除 1 后，数组为空
        ([5, 6, 7], 8, 3),  # 删除 8 后，数组不变
        ([10], 10, 0),  # 删除唯一元素 10
        ([], 1, 0),  # 空数组
    ]
    
    for i, (nums, val, expected) in enumerate(test_cases, 1):
        result = sol.removeElement(nums, val)
        print(f"Test case {i}:")
        print(f"Input: {nums}, val: {val}")
        print(f"Expected: {expected}, Result: {result}")
        print(f"Modified array: {nums[:result]}")  # 打印修改后的有效部分
        print("✅ Pass" if result == expected else "❌ Fail")
        print("-" * 40)

if __name__ == "__main__":
    test()
