/**
 * 给定长度为 2n 的整数数组 nums ，你的任务是将这些数分成 n 对, 例如 (a1, b1), (a2, b2), ..., (an, bn) ，使得从 1 到 n 的 min(ai, bi) 总和最大。
 * 返回该 最大总和 。
 */


import java.util.Arrays;

class Solution {
    public int arrayPairSum(int[] nums) {
        Arrays.sort(nums);
        int sum = 0;
        for (int i = 0; i < nums.length; i++) {
            if (i % 2 == 0) {
                sum += nums[i];
            }
        }
        return sum;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        
        // 定义测试用例：每个测试用例由输入数组和期望的结果组成
        Object[][] testCases = {
            {new int[]{1, 4, 3, 2}, 4},   // 期望结果：4
            {new int[]{6, 2, 6, 5, 1, 2}, 9}, // 期望结果：9
            {new int[]{1, 1, 1, 1}, 2},  // 期望结果：2
            {new int[]{1000, 1000, 1000, 1000}, 2000},  // 期望结果：2000
            {new int[]{-1, -2, -3, -4}, -4},  // 期望结果：-4
            {new int[]{5, 7, 9, 1, 3, 6}, 12}  // 期望结果：12
        };
        
        // 循环遍历每个测试用例
        for (int i = 0; i < testCases.length; i++) {
            int[] input = (int[]) testCases[i][0];
            int expected = (int) testCases[i][1];
            int result = sol.arrayPairSum(input);
            
            // 输出测试信息
            System.out.printf("Test %d: nums=%s\n", i + 1, Arrays.toString(input));
            System.out.printf("Expected: %d, Result: %d\n", expected, result);
            System.out.println(result == expected ? "✅ Pass" : "❌ Fail");
            System.out.println("-".repeat(40));
        }
    }
}
