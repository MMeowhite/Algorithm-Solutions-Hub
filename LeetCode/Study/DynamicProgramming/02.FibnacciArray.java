package LeetCode.Study.DynamicProgramming;

/*
 * 斐波那契数 （通常用 F(n) 表示）形成的序列称为 斐波那契数列 。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：
 * F(0) = 0，F(1) = 1
 * F(n) = F(n - 1) + F(n - 2)，其中 n > 1
 * 给定 n ，请计算 F(n) 。
 */

class Solution {
    public int fib(int n) {
        if (n == 0) {
            return 0;
        }

        if (n == 1){
            return 1;
        }
        int a = 0, b = 1;
        for (int i = 2; i < n + 1; i++){
            int temp = b;
            b = a + b;
            a = temp;
        }

        return b;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        int[] testCases = {0, 1, 2, 3, 5, 10, 20, 30};
        int[] expectedResults = {0, 1, 1, 2, 5, 55, 6765, 832040};

        for (int i = 0; i < testCases.length; i++) {
            int n = testCases[i];
            int expected = expectedResults[i];
            int actual = solution.fib(n);

            System.out.print("Test case " + (i + 1) + ": ");
            System.out.print("n = " + n);
            System.out.print(", Expected = " + expected);
            System.out.println(", Actual = " + actual + (expected == actual ? " ✅ Pass" : " ❌ Fail"));
        }
    }
}