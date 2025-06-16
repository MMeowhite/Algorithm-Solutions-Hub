/*
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
请必须使用时间复杂度为 O(log n) 的算法。
*/

class Solution {
    public int searchInsert(int[] nums, int target) {
        int start = 0;
        int end = nums.length - 1;

        while (start <= end) {
            int mid = (start + end) / 2;
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] <= target) {
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }

        return start;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        int[][] testCases = {
                { 1, 3, 5, 6 },
                { 1, 3, 5, 6 },
                { 1, 3, 5, 6 },
                { 1, 3, 5, 6 },
                { 1 },
                { 1 },
                { 1 }
        };

        int[] targets = { 5, 2, 7, 0, 0, 1, 2 };
        int[] expected = { 2, 1, 4, 0, 0, 0, 1 };

        for (int i = 0; i < testCases.length; i++) {
            int result = solution.searchInsert(testCases[i], targets[i]);
            System.out.print("Test case " + (i + 1) + ": ");
            System.out.print("Input = " + java.util.Arrays.toString(testCases[i]));
            System.out.print(", target = " + targets[i]);
            System.out.print(", expected = " + expected[i]);
            System.out.println(", result = " + result + (result == expected[i] ? " ✅ Pass" : " ❌ Fail"));
        }
    }
}