/**
 * 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
 * 请注意 ，必须在不复制数组的情况下原地对数组进行操作。
 */

class Solution {
    public void moveZeroes(int[] nums) {
        int lastNonZeroIndex = 0;

        // 先把所有非零元素按顺序移到前面
        for (int current = 0; current < nums.length; current++) {
            if (nums[current] != 0) {
                nums[lastNonZeroIndex] = nums[current];
                lastNonZeroIndex++;
            }
        }

        // 把剩下的位子补0
        for (int i = lastNonZeroIndex; i < nums.length; i++) {
            nums[i] = 0;
        }
    }
    
    public static void main(String[] args) {
        Solution sol = new Solution();

        int[][] testInputs = {
            {0, 1, 0, 3, 12},
            {0, 0, 1},
            {1, 2, 3},
            {0, 0, 0},
            {},
            {4, 0, 0, 1, 0, 3, 0, 5}
        };

        int[][] expectedOutputs = {
            {1, 3, 12, 0, 0},
            {1, 0, 0},
            {1, 2, 3},
            {0, 0, 0},
            {},
            {4, 1, 3, 5, 0, 0, 0, 0}
        };

        for (int i = 0; i < testInputs.length; i++) {
            int[] input = testInputs[i];
            sol.moveZeroes(input);

            System.out.println("Test case " + (i + 1) + ":");
            System.out.print("Result:   ");
            printArray(input);
            System.out.print("Expected: ");
            printArray(expectedOutputs[i]);
            System.out.println(compareArrays(input, expectedOutputs[i]) ? "✅ Pass" : "❌ Fail");
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

    private static boolean compareArrays(int[] a, int[] b) {
        if (a.length != b.length) return false;
        for (int i = 0; i < a.length; i++) {
            if (a[i] != b[i]) return false;
        }
        return true;
    }
}