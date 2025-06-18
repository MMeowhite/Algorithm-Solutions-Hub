"""
给你一个字符串 s ，请你反转字符串中 单词 的顺序。
单词 是由非空格字符组成的字符串。s 中使用至少一个空格将字符串中的 单词 分隔开。
返回 单词 顺序颠倒且 单词 之间用单个空格连接的结果字符串。
注意：输入字符串 s中可能会存在前导空格、尾随空格或者单词间的多个空格。返回的结果字符串中，单词间应当仅用单个空格分隔，且不包含任何额外的空格。
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        """
        反转字符串中单词的顺序
        
        参数:
            s: 输入字符串（可能包含前导/尾随/多个空格)
        
        返回:
            单词顺序反转且用单个空格连接的结果字符串
        """
        # 1. 去除首尾空格
        s = s.strip()
        # 2. 分割单词（处理多个空格情况）
        words = s.split()
        # 3. 反转单词列表
        words.reverse()
        # 4. 用单个空格连接单词
        return ' '.join(words)

        # 一行代码
        # return (' ').join(s.split()[::-1])


def test():
    sol = Solution()
    
    test_cases = [
        ("the sky is blue", "blue is sky the"),
        ("  hello world  ", "world hello"),
        ("a good   example", "example good a"),
        ("  Bob    Loves  Alice   ", "Alice Loves Bob"),
        ("Alice does not even like bob", "bob like even not does Alice"),
        ("", ""),  # 空字符串
        ("   ", ""),  # 纯空格
        ("single", "single"),  # 单个单词
        ("  a  b  c  ", "c b a"),  # 单个字符单词
        ("!@# $% ^&*", "^&* $% !@#")  # 特殊字符
    ]
    
    for i, (input_str, expected) in enumerate(test_cases, 1):
        result = sol.reverseWords(input_str)
        print(f"Test case {i}:")
        print(f"Input:    '{input_str}'")
        print(f"Expected: '{expected}'")
        print(f"Result:   '{result}'")
        print("✅ Pass" if result == expected else "❌ Fail")
        print("-" * 40)


if __name__ == "__main__":
    test()