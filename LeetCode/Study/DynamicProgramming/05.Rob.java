package LeetCode.Study.DynamicProgramming;
/*
 * 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
 * 给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
 */

import java.util.Arrays;

class Solution {
    public int rob(int[] nums) {
        int n = nums.length;
        if (n == 0) return 0;
        if (n == 1) return nums[0];

        int prev2 = nums[0];
        int prev1 = Math.max(nums[0], nums[1]);

        for (int i = 2; i < n; i++) {
            // 要么不偷第 i 间，收益是 dp[i - 1]；要么偷第 i 间，那就不能偷 i - 1，收益是 dp[i - 2] + nums[i]。
            int cur = Math.max(prev1, prev2 + nums[i]);
            prev2 = prev1;
            prev1 = cur;
        }

        return prev1;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        int[][] testCases = {
            {1, 2, 3, 1},           // → 4
            {2, 7, 9, 3, 1},        // → 12
            {2, 1, 1, 2},           // → 4
            {5},                   // → 5
            {1, 2},                // → 2
            {0, 0, 0},             // → 0
            {100, 1, 1, 100},      // → 200
            {},                    // → 0
        };

        int[] expectedResults = {
            4, 12, 4, 5, 2, 0, 200, 0
        };

        for (int i = 0; i < testCases.length; i++) {
            int[] nums = testCases[i];
            int expected = expectedResults[i];
            int actual = solution.rob(nums);

            System.out.print("Test case " + (i + 1) + ": ");
            System.out.print("nums = " + Arrays.toString(nums));
            System.out.print(", Expected = " + expected);
            System.out.println(", Actual = " + actual + (expected == actual ? " ✅ Pass" : " ❌ Fail"));
        }
    }
}
