"""
给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0 开始）。
如果 needle 不是 haystack 的一部分，则返回  -1 。
"""

class Solution:
    def strStr(self, haystack, needle: str) -> int:
        if not needle:
            return 0
        
        n, m = len(haystack), len(needle)
        if m > n:
            return -1

        for i in range(n - m + 1):
            if haystack[i:i+m] == needle:
                return i
        return -1

# 测试代码
def test():
    sol = Solution()
    test_cases = [
        ("hello", "ll", 2),
        ("aaaaa", "bba", -1),
        ("", "", 0),
        ("abc", "c", 2),
        ("mississippi", "issip", 4),
        ("a", "a", 0),
        ("abc", "abcd", -1)
    ]
    
    for i, (haystack, needle, expected) in enumerate(test_cases, 1):
        result = sol.strStr(haystack, needle)
        print(f"Test case {i}:")
        print(f"Haystack: '{haystack}', Needle: '{needle}'")
        print(f"Expected: {expected}, Result: {result}")
        print("✅ Pass" if result == expected else "❌ Fail")
        print("-" * 40)

if __name__ == "__main__":
    test()