
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return []
    
def test():
    sol = Solution()
    test_cases = [
        ([2, 7, 11, 15], 9, [1, 2]),
        ([1, 2, 3, 4, 4, 9, 56, 90], 8, [4, 5]),
        ([2, 3, 4], 6, [1, 3]),
        ([-1, 0], -1, [1, 2]),
        ([5, 25, 75], 100, [2, 3]),
        ([1, 3, 4, 5, 7, 11, 15], 9, [3, 4]),
    ]

    for i, (numbers, target, expected) in enumerate(test_cases, 1):
        result = sol.twoSum(numbers, target)
        print(f"Test case {i}:")
        print(f"Input: numbers = {numbers}, target = {target}")
        print(f"Expected: {expected}, Result: {result}")
        print("✅ Pass" if result == expected else "❌ Fail")
        print("-" * 40)

if __name__ == "__main__":
    test()