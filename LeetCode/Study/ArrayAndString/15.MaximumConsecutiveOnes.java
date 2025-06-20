/*
 * 给定一个二进制数组 nums ， 计算其中最大连续 1 的个数。
 */

class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int maxCount = 0, count = 0;
        for (int num : nums) {
            if (num == 1) {
                count++;
                maxCount = Math.max(maxCount, count);
            } else {
                count = 0;
            }
        }
        return maxCount;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        
        // 测试用例
        int[][] testCases = {
            {1, 1, 0, 1, 1, 1},
            {1, 0, 1, 1, 0, 1},
            {0, 0, 0, 0},
            {1, 1, 1, 1},
            {1, 0, 1, 1, 0, 1, 1}
        };
        
        for (int i = 0; i < testCases.length; i++) {
            int[] nums = testCases[i];
            int result = sol.findMaxConsecutiveOnes(nums);
            
            // 打印输出
            System.out.printf("Test %d: nums=%s\n", i + 1, java.util.Arrays.toString(nums));
            System.out.printf("Max consecutive ones: %d\n", result);
            System.out.println("-".repeat(40));
        }
    }
}