/*
 * 给你一个下标从 1 开始的整数数组 numbers ，该数组已按 非递减顺序排列  ，请你从数组中找出满足相加之和等于目标数 target 的两个数。如果设这两个数分别是 numbers[index1] 和 numbers[index2] ，则 1 <= index1 < index2 <= numbers.length 。
 * 以长度为 2 的整数数组 [index1, index2] 的形式返回这两个整数的下标 index1 和 index2。
 * 你可以假设每个输入 只对应唯一的答案 ，而且你 不可以 重复使用相同的元素。
 * 你所设计的解决方案必须只使用常量级的额外空间。
 */

import java.util.Arrays;

class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int left = 0, right = numbers.length - 1;

        while (left < right) {
            int sum = numbers[left] + numbers[right];
            if (sum == target) {
                return new int[] { left + 1, right + 1 }; // 返回下标从 1 开始
            } else if (sum < target) {
                left++; // 如果和小于目标值，移动左指针向右
            } else {
                right--; // 如果和大于目标值，移动右指针向左
            }
        }

        return new int[] {}; // 如果没有找到，返回空数组
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        // 定义测试用例：每个测试用例由输入数组、目标值以及期望结果组成
        Object[][] testCases = {
            {new int[]{2, 7, 11, 15}, 9, new int[]{1, 2}},  // 期望返回 {1, 2}
            {new int[]{1, 2, 3, 4, 5}, 5, new int[]{1, 4}}, // 期望返回 {1, 4}
            {new int[]{1, 3, 4, 5, 6, 10}, 11, new int[]{2, 5}}, // 期望返回 {2, 5}
            {new int[]{-1, 0, 3, 5, 6}, 4, new int[]{1, 4}},  // 期望返回 {1, 4}
            {new int[]{-2, -1, 0, 1, 3}, 2, new int[]{3, 5}},  // 期望返回 {3, 5}
            {new int[]{-5, -3, -1, 0, 1, 4, 7}, 6, new int[]{3, 7}},  // 期望返回 {3, 7}
        };

        // 循环遍历每个测试用例
        for (int i = 0; i < testCases.length; i++) {
            int[] input = (int[]) testCases[i][0];
            int target = (int) testCases[i][1];
            int[] expected = (int[]) testCases[i][2];
            int[] result = sol.twoSum(input, target);

            // 输出测试信息
            System.out.printf("Test %d: nums=%s, target=%d\n", i + 1, Arrays.toString(input), target);
            System.out.printf("Expected: %s, Result: %s\n", Arrays.toString(expected), Arrays.toString(result));
            System.out.println(Arrays.equals(result, expected) ? "✅ Pass" : "❌ Fail");
            System.out.println("-".repeat(40));
        }
    }
}