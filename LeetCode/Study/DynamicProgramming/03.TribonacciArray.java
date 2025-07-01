package LeetCode.Study.DynamicProgramming;

/*
 * T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2
 * 给你整数 n，请返回第 n 个泰波那契数 Tn 的值。
 */

class Solution {
    public int tribonacci(int n) {
        if (n == 0) return 0;
        if (n == 1 || n == 2) return 1;
        
        int t0 = 0, t1 = 1, t2 = 1;
        for (int i = 3; i < n + 1; i++){
            int temp = t0 + t1 + t2;
            t0 = t1;
            t1 = t2;
            t2 = temp;
        }

        return t2;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        int[] testCases = {0, 1, 2, 3, 4, 5, 10, 20, 25};
        int[] expectedResults = {0, 1, 1, 2, 4, 7, 149, 35890, 1389537};

        for (int i = 0; i < testCases.length; i++) {
            int n = testCases[i];
            int expected = expectedResults[i];
            int actual = solution.tribonacci(n);

            System.out.print("Test case " + (i + 1) + ": ");
            System.out.print("n = " + n);
            System.out.print(", Expected = " + expected);
            System.out.println(", Actual = " + actual + (expected == actual ? " ✅ Pass" : " ❌ Fail"));
        }
    }
}

