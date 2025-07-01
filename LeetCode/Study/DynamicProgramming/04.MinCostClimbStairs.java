package LeetCode.Study.DynamicProgramming;

/*
 * 给你一个整数数组 cost ，其中 cost[i] 是从楼梯第 i 个台阶向上爬需要支付的费用。一旦你支付此费用，即可选择向上爬一个或者两个台阶。
 * 你可以选择从下标为 0 或下标为 1 的台阶开始爬楼梯。
 * 请你计算并返回达到楼梯顶部的最低花费。
 */

import java.util.Arrays;

class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int a = cost[0], b = cost[1];
        for (int i = 2; i < cost.length; i++){
            int temp = cost[i] + Math.min(a, b);
            a = b;
            b = temp;
        }
        return Math.min(a, b);
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        int[][] testCases = {
            {10, 15, 20},           // → 最少花费 15
            {1, 100, 1, 1, 1, 100, 1, 1, 100, 1}, // → 最少花费 6
            {0, 2, 2, 1},           // → 最少花费 2
            {1, 2},                 // → 最少花费 1
            {5, 5, 5, 5},           // → 最少花费 10
            {0, 0, 0, 1},           // → 最少花费 0
            {1, 100},               // → 最少花费 1
        };

        int[] expectedResults = {
            15, 6, 2, 1, 10, 0, 1
        };

        for (int i = 0; i < testCases.length; i++) {
            int[] cost = testCases[i];
            int expected = expectedResults[i];
            int actual = solution.minCostClimbingStairs(cost);

            System.out.print("Test case " + (i + 1) + ": ");
            System.out.print("cost = " + Arrays.toString(cost));
            System.out.print(", Expected = " + expected);
            System.out.println(", Actual = " + actual + (expected == actual ? " ✅ Pass" : " ❌ Fail"));
        }
    }
}
