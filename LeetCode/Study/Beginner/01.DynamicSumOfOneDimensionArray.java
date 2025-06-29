/*
 * 给你一个数组 nums 。数组「动态和」的计算公式为：runningSum[i] = sum(nums[0]…nums[i]) 。
 * 请返回 nums 的动态和。
 */

import java.util.Arrays;

class Solution {
    public int[] runningSum(int[] nums) {
        int[] dynamicSum = new int[nums.length];
        int currentSum = 0;
        
        for (int i = 0; i < nums.length; i++) {
            currentSum += nums[i];
            dynamicSum[i] = currentSum;
        }
        
        return dynamicSum;

        // int n = nums.length;
        // for (int i = 1; i < n; i++) {
        //     nums[i] += nums[i - 1];
        // }
        // return nums;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        int[][] testCases = {
            {1, 2, 3, 4},
            {1, 1, 1, 1, 1},
            {3, 1, 2, 10, 1},
            {},
            {5}
        };

        int[][] expectedResults = {
            {1, 3, 6, 10},
            {1, 2, 3, 4, 5},
            {3, 4, 6, 16, 17},
            {},
            {5}
        };

        for (int i = 0; i < testCases.length; i++) {
            int[] actual = solution.runningSum(testCases[i]);
            System.out.print("Test case " + (i + 1) + ": ");
            System.out.print("Input = " + Arrays.toString(testCases[i]));
            System.out.print(", Expected = " + Arrays.toString(expectedResults[i]));
            System.out.println(", Actual = " + Arrays.toString(actual) + (Arrays.equals(actual, expectedResults[i]) ? " ✅ Pass" : " ❌ Fail"));
        }
    }
}