// 给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素。元素的顺序可能发生改变。然后返回 nums 中与 val 不同的元素的数量。
// 假设 nums 中不等于 val 的元素数量为 k，要通过此题，您需要执行以下操作：
// 更改 nums 数组，使 nums 的前 k 个元素包含不等于 val 的元素。nums 的其余元素和 nums 的大小并不重要。
// 返回 k。
// 用户评测：

// 评测机将使用以下代码测试您的解决方案：

// int[] nums = [...]; // 输入数组
// int val = ...; // 要移除的值
// int[] expectedNums = [...]; // 长度正确的预期答案。
//                             // 它以不等于 val 的值排序。

// int k = removeElement(nums, val); // 调用你的实现

// assert k == expectedNums.length;
// sort(nums, 0, k); // 排序 nums 的前 k 个元素
// for (int i = 0; i < actualLength; i++) {
//     assert nums[i] == expectedNums[i];
// }
// 如果所有的断言都通过，你的解决方案将会 通过。

class Solution {
    public int removeElement(int[] nums, int val) {
        int slow = 0, count = 0;
        for (int fast = 0; fast < nums.length; fast++) {
            if (nums[fast] != val) {
                nums[slow] = nums[fast];
                slow++;
                count++;
            } else {
                nums[slow] = 0;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        // 测试用例
        int[][] testCases = {
            {3, 2, 2, 3},
            {0, 1, 2, 2, 3, 0, 4, 2},
            {2, 2, 2, 2},
            {1, 2, 3, 4},
            {1, 1, 1, 1}
        };
        int[] values = {3, 2, 2, 1}; // 每个测试用例对应的 val

        for (int i = 0; i < testCases.length; i++) {
            int[] nums = testCases[i];
            int val = values[i];
            int len = sol.removeElement(nums, val);

            // 打印输出
            System.out.printf("Test %d: nums=%s, val=%d\n", i + 1, java.util.Arrays.toString(nums), val);
            System.out.printf("New length: %d, Updated array: %s\n", len, java.util.Arrays.toString(java.util.Arrays.copyOfRange(nums, 0, len)));
            System.out.println("-".repeat(40));
        }
    }
}