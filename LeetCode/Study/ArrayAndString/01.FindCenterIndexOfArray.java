/*
给你一个整数数组:nums ，请计算数组的 中心下标 。
数组 中心下标 是数组的一个下标，其左侧所有元素相加的和等于右侧所有元素相加的和。
如果中心下标位于数组最左端，那么左侧数之和视为 0 ，因为在下标的左侧不存在元素。这一点对于中心下标位于数组最右端同样适用。
如果数组有多个中心下标，应该返回 最靠近左边 的那一个。如果数组不存在中心下标，返回 -1 。

*/

class Solution {
    public int pivotIndex(int[] nums) {
        int totalSum = 0;
        for (int num : nums) {
            totalSum += num;
        }

        int leftSum = 0;
        for (int i = 0; i < nums.length; i++) {
            // right sum = total - left - current
            if (leftSum == totalSum - leftSum - nums[i]) {
                return i;
            }
            leftSum += nums[i];
        }

        return -1;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // 定义测试用例数组
        int[][] testCases = {
                { 1, 7, 3, 6, 5, 6 }, // 输出应为 3
                { 1, 2, 3 }, // 输出应为 -1
                { 2, 1, -1 }, // 输出应为 0
                { 0, 0, 0 }, // 输出应为 0
                { 1 }, // 输出应为 0
                { 1, -1, 0 }, // 输出应为 2
        };

        int[] expectedResults = { 3, -1, 0, 0, 0, 2 };

        // 遍历每个测试用例
        for (int i = 0; i < testCases.length; i++) {
            int[] nums = testCases[i];
            int expected = expectedResults[i];
            int actual = solution.pivotIndex(nums);

            System.out.print("Test case " + (i + 1) + ": ");
            System.out.print("Input = " + java.util.Arrays.toString(nums));
            System.out.print(", Expected = " + expected);
            System.out.println(", Actual = " + actual + (expected == actual ? " ✅ Pass" : " ❌ Fail"));
        }
    }
}