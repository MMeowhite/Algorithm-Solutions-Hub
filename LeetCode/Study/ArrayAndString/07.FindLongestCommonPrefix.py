"""
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。
"""

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # 以第一个字符串作为基准
        base = strs[0]
        
        for i in range(len(base)):
            for s in strs[1:]:  # 从第二个字符串开始比较
                # 如果当前字符串长度不够，或者字符不匹配
                if i >= len(s) or s[i] != base[i]:
                    return base[:i]
        
        # 如果全部匹配，返回整个基准字符串
        return base
    
def test():
    sol = Solution()

    test_cases = [
        (
            ["flower", "flow", "flight"],
            "fl"
        ),
        (
            ["dog", "racecar", "car"],
            ""
        ),
        (
            ["a"],
            "a"
        ),
        (
            ["", ""],
            ""
        ),
        (
            [],
            ""
        ),
        (
            ["apple", "appetite", "application"],
            "app"
        ),
        (
            ["same", "same", "same"],
            "same"
        ),
        (
            ["prefix", "preface", "premium"],
            "pre"
        )
    ]

    for i, (input_strs, expected) in enumerate(test_cases, 1):
        result = sol.longestCommonPrefix(input_strs)
        print(f"Test case {i}:")
        print(f"Input:    {input_strs}")
        print(f"Expected: {expected}")
        print(f"Result:   {result}")
        print("✅ Pass" if result == expected else "❌ Fail")
        print("-" * 40)


if __name__ == "__main__":
    test()