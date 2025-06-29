"""
给你两个字符串：ransomNote 和 magazine ，判断 ransomNote 能不能由 magazine 里面的字符构成。
如果可以，返回 true ；否则返回 false 。
magazine 中的每个字符只能在 ransomNote 中使用一次。
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counts = [0] * 26

        for c in magazine:
            counts[ord(c) - ord('a')] += 1
        
        for c in ransomNote:
            index = ord(c) - ord('a')
            counts[index] -= 1
            if counts[index] < 0:
                return False
        
        return True
    
def test():
    sol = Solution()

    test_cases = [
        ("a", "b", False),
        ("aa", "ab", False),
        ("aa", "aab", True),
        ("abc", "aabbcc", True),
        ("abc", "def", False),
        ("", "anything", True),
        ("a", "a", True),
        ("aaa", "aa", False)
    ]

    for i, (ransomNote, magazine, expected) in enumerate(test_cases):
        result = sol.canConstruct(ransomNote, magazine)
        print(f"Test case {i+1}: ransomNote = '{ransomNote}', magazine = '{magazine}'")
        print(f"Expected: {expected}, Got: {result}")
        print("Pass ✅" if result == expected else "Fail ❌")
        print("-" * 40)

if __name__ == "__main__":
    test()