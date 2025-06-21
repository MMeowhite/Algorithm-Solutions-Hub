/*
 * 给你一个 非严格递增排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。元素的 相对顺序 应该保持 一致 。然后返回 nums 中唯一元素的个数。
 * 考虑 nums 的唯一元素的数量为 k ，你需要做以下事情确保你的题解可以被通过：
 * 更改数组 nums ，使 nums 的前 k 个元素包含唯一元素，并按照它们最初在 nums 中出现的顺序排列。nums 的其余元素与 nums 的大小不重要。
 * 返回 k 。
 */

class Solution {
    public int removeDuplicates(int[] nums) {
        int i = 0;

        for (int j = 0; j < nums.length; j++){
            if (nums[j] != nums[i]){
                i = i + 1;
                nums[i] = nums[j];
            }
        }
        
        return i + 1;
    }
    
    public static void main(String[] args) {
        Solution sol = new Solution();

        int[][] testInputs = {
            {1, 1, 2},
            {0, 0, 1, 1, 1, 2, 2, 3, 3, 4},
            {1, 2, 3, 4, 5},
            {1, 1, 1, 1},
            {},
            {1}
        };

        int[][] expectedOutputs = {
            {1, 2},
            {0, 1, 2, 3, 4},
            {1, 2, 3, 4, 5},
            {1},
            {},
            {1}
        };

        for (int i = 0; i < testInputs.length; i++) {
            int[] input = testInputs[i];
            int k = sol.removeDuplicates(input);

            System.out.println("Test case " + (i + 1) + ":");
            System.out.print("Input after processing: ");
            printArray(input, k);
            System.out.print("Expected: ");
            printArray(expectedOutputs[i], expectedOutputs[i].length);
            boolean isPass = compareArrays(input, expectedOutputs[i], k);
            System.out.println(isPass ? "✅ Pass" : "❌ Fail");
            System.out.println("----------------------------------------");
        }
    }

    private static void printArray(int[] arr, int length) {
        System.out.print("[");
        for (int i = 0; i < length; i++) {
            System.out.print(arr[i]);
            if (i < length - 1) System.out.print(", ");
        }
        System.out.println("]");
    }

    private static boolean compareArrays(int[] actual, int[] expected, int length) {
        if (length != expected.length) return false;
        for (int i = 0; i < length; i++) {
            if (actual[i] != expected[i]) return false;
        }
        return true;
    }
}