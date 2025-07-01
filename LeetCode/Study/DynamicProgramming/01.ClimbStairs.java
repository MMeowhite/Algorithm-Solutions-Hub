/*
 * 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
 * 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
 */

package LeetCode.Study.DynamicProgramming;

class Solution {
    public int climbStairs(int n) {
        if (n <= 2) {
            return n;
        }

        int a = 1; // 第1阶有1种方法
        int b = 2; // 第2阶有2种方法

        for (int i = 3; i <= n; i++) {
            int temp = a + b;
            a = b;
            b = temp;
        }

        return b;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        int[] testCases = {
            1, 2, 3, 4, 5, 10, 20, 30
        };

        int[] expectedResults = {
            1, 2, 3, 5, 8, 89, 10946, 1346269
        };

        for (int i = 0; i < testCases.length; i++) {
            int n = testCases[i];
            int expected = expectedResults[i];
            int actual = solution.climbStairs(n);

            System.out.print("Test case " + (i + 1) + ": ");
            System.out.print("n = " + n);
            System.out.print(", Expected = " + expected);
            System.out.println(", Actual = " + actual + (expected == actual ? " ✅ Pass" : " ❌ Fail"));
        }
    }
}