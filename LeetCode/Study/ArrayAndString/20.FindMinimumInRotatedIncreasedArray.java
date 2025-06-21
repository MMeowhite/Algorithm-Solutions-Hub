/*
 * 已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转 后，得到输入数组。例如，原数组 nums = [0,1,2,4,5,6,7] 在变化后可能得到：
 * 若旋转 4 次，则可以得到 [4,5,6,7,0,1,2]
 * 若旋转 7 次，则可以得到 [0,1,2,4,5,6,7]
 * 注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], ..., a[n-2]] 。
 * 给你一个元素值 互不相同 的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。
 * 你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。
 */

class Solution {
    public int findMin(int[] nums) {
        int left = 0, right = nums.length - 1;

        while (left < right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] > nums[right]) {
                // 中间元素大于右边界元素，说明最小值在右半部分
                left = mid + 1;
            } else {
                // 中间元素小于等于右边界元素，说明最小值在左半部分或中间
                right = mid;
            }
        }

        return nums[left]; // 此时 left == right，指向最小值
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        int[][] testInputs = {
            {3, 4, 5, 1, 2},
            {4, 5, 6, 7, 0, 1, 2},
            {11, 13, 15, 17},
            {2, 1},
            {1},
            {2, 3, 4, 5, 1},
            {1, 2, 3, 4, 5}, // 未旋转
            {5, 1, 2, 3, 4}  // 旋转1次
        };

        int[] expectedOutputs = {
            1,
            0,
            11,
            1,
            1,
            1,
            1,
            1
        };

        for (int i = 0; i < testInputs.length; i++) {
            int[] input = testInputs[i];
            int expected = expectedOutputs[i];
            int result = sol.findMin(input);

            System.out.println("Test case " + (i + 1) + ":");
            System.out.print("Input: ");
            printArray(input);
            System.out.println("Expected: " + expected);
            System.out.println("Result:   " + result);
            System.out.println(expected == result ? "✅ Pass" : "❌ Fail");
            System.out.println("----------------------------------------");
        }
    }

    private static void printArray(int[] arr) {
        System.out.print("[");
        for (int j = 0; j < arr.length; j++) {
            System.out.print(arr[j]);
            if (j < arr.length - 1) System.out.print(", ");
        }
        System.out.println("]");
    }
}