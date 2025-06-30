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
}