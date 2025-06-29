"""
给你一个整数 n ，返回一个字符串数组 answer（下标从 1 开始），其中：
answer[i] == "FizzBuzz" 如果 i 同时是 3 和 5 的倍数。
answer[i] == "Fizz" 如果 i 是 3 的倍数。
answer[i] == "Buzz" 如果 i 是 5 的倍数。
answer[i] == i （以字符串形式）如果上述条件全不满足。
"""

from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []

        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                answer.append("FizzBuzz")
            elif i % 3 == 0:
                answer.append("Fizz")
            elif i % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(i))
        
        return answer
    
def test():
    sol = Solution()

    test_cases = [
        (1, ["1"]),
        (3, ["1", "2", "Fizz"]),
        (5, ["1", "2", "Fizz", "4", "Buzz"]),
        (15, ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]),
        (0, []),
    ]

    for i, (n, expected) in enumerate(test_cases):
        result = sol.fizzBuzz(n)
        print(f"Test case {i+1}: n = {n}")
        print(f"Expected: {expected}")
        print(f"Got:      {result}")
        print("Pass ✅" if result == expected else "Fail ❌")
        print("-" * 40)

if __name__ == "__main__":
    test()