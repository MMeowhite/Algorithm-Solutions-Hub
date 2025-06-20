/*
 * 给定一个含有 n 个正整数的数组和一个正整数 target 。
 * 找出该数组中满足其总和大于等于 target 的长度最小的 子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。
 * 如果不存在符合条件的子数组，返回 0 。
 */

import java.util.Arrays;

class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int minLength = Integer.MAX_VALUE, left = 0, current_sum = 0;

        for (int right = 0; right < nums.length; right++) {
            current_sum += nums[right]; // 扩大窗口，增加右边界

            // 当当前窗口的和大于等于目标值时，尝试缩小窗口
            while (current_sum >= target) {
                minLength = Math.min(minLength, right - left + 1); // 更新最小长度
                current_sum -= nums[left]; // 缩小窗口，减少左边界
                left++;
            }
        }

        return minLength == Integer.MAX_VALUE ? 0 : minLength; // 如果没有找到满足条件的子数组，返回0
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        int[][] testArrays = {
            {2, 3, 1, 2, 4, 3}, // expected: 2
            {1, 4, 4},          // expected: 1
            {1, 1, 1, 1, 1, 1, 1, 1}, // expected: 0
            {1, 2, 3, 4, 5},    // expected: 2
            {5, 1, 3, 5, 10, 7, 4, 9, 2, 8} // expected: 2
        };
        int[] targets = {
            7,
            4,
            11,
            11,
            15
        };
        int[] expected = {
            2,
            1,
            0,
            3,
            2
        };

        for (int i = 0; i < testArrays.length; i++) {
            int result = sol.minSubArrayLen(targets[i], testArrays[i]);
            System.out.println("Test " + (i + 1));
            System.out.println("Input array: " + Arrays.toString(testArrays[i]));
            System.out.println("Target: " + targets[i]);
            System.out.println("Expected: " + expected[i] + ", Got: " + result);
            System.out.println(result == expected[i] ? "✅ Pass" : "❌ Fail");
            System.out.println("-".repeat(40));
        }
    }
}

