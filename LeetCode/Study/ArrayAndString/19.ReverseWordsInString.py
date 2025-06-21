"""
给定一个字符串 s ，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        reversed_words = [word[::-1] for word in words]
        return ' '.join(reversed_words)
    
        # return " ".join([word[::-1] for word in s.split()])

def test():
    sol = Solution()
    test_cases = [
        ("Let's take LeetCode contest", "s'teL ekat edoCteeL tsetnoc"),  # 每个单词反转
        ("Hello World", "olleH dlroW"),  # 两个单词反转
        ("a b c", "a b c"),  # 单个字符单词
        ("", ""),  # 空字符串
        ("   ", "   "),  # 只有空格
    ]
    
    for i, (s, expected) in enumerate(test_cases, 1):
        result = sol.reverseWords(s)
        print(f"Test case {i}:")
        print(f"Input: '{s}'")
        print(f"Expected: '{expected}', Result: '{result}'")
        print("✅ Pass" if result == expected else "❌ Fail")
        print("-" * 40)

if __name__ == "__main__":
    test()