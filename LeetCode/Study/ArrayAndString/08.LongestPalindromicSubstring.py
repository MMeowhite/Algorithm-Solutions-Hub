"""
给你一个字符串 s，找到 s 中最长的 回文 子串。
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_aroud_center(left: int, right: int) -> str:
            """中心扩展函数"""
            while left >= 0 and right < len(s) and s[left]==s[right]:
                left -= 1
                right += 1
            
            return s[left+1:right] # 返回找到的回文字串
        
        if not s:
            return ""
        
        result = ""
        for i in range(len(s)):
            odd = expand_aroud_center(i, i)
            even = expand_aroud_center(i, i + 1)

            # 更新最长回文子串
            if len(odd) > len(result):
                result = odd
            if len(even) > len(result):
                result = even

        return result
    
def test():
    sol = Solution()
    
    test_cases = [
        ("babad", ["bab", "aba"]),  # 多个有效答案
        ("cbbd", ["bb"]),
        ("a", ["a"]),
        ("ac", ["a", "c"]),  # 多个有效单字符答案
        ("racecar", ["racecar"]),
        ("", [""]),
        ("abb", ["bb"]),
        ("abcba", ["abcba"]),
        ("aaabaaaa", ["aaabaaa"]),
    ]
    
    for i, (input_str, expected) in enumerate(test_cases, 1):
        result = sol.longestPalindrome(input_str)
        print(f"Test case {i}:")
        print(f"Input:    {input_str}")
        print(f"Expected: {expected}")
        print(f"Result:   {result}")
        print("✅ Pass" if result in expected else "❌ Fail")
        print("-" * 40)

if __name__ == "__main__":
    test()