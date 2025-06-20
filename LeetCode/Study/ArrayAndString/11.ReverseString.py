"""
编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 s 的形式给出。
不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
"""

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left+=1
            right-=1

def test():
    sol = Solution()
    test_cases = [
        (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
        (["a", "b", "c", "d", "e"], ["e", "d", "c", "b", "a"]),
        (["r", "a", "c", "e", "c", "a", "r"], ["r", "a", "c", "e", "c", "a", "r"]),  # palindrome
        (["a", "b", "c"], ["c", "b", "a"]),
        (["x", "y", "z"], ["z", "y", "x"]),
        (["a"], ["a"]),  # single character (edge case)
        ([], []),  # empty string (edge case)
    ]
    
    for i, (input_str, expected) in enumerate(test_cases, 1):
        sol.reverseString(input_str)
        print(f"Test case {i}:")
        print(f"Input: {input_str}")
        print(f"Expected: {expected}, Result: {input_str}")
        print("✅ Pass" if input_str == expected else "❌ Fail")
        print("-" * 40)

if __name__ == "__main__":
    test()

