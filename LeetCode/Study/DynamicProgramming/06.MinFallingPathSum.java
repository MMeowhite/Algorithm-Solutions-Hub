/*
 * 给你一个 n x n 的 方形 整数数组 matrix ，请你找出并返回通过 matrix 的下降路径 的 最小和 。
 * 下降路径 可以从第一行中的任何元素开始，并从每一行中选择一个元素。
 * 在下一行选择的元素和当前行所选元素最多相隔一列（即位于正下方或者沿对角线向左或者向右的第一个元素）。
 * 具体来说，位置 (row, col) 的下一个元素应当是 (row + 1, col - 1)、(row + 1, col) 或者 (row + 1, col + 1) 。
 */
package LeetCode.Study.DynamicProgramming;

import java.util.Arrays;

class Solution {
    public int minFallingPathSum(int[][] matrix) {
        int n = matrix.length;

        // 从倒数第二行往上处理
        for (int i = n - 2; i >= 0; i--) {
            for (int j = 0; j < n; j++) {
                // 获取左下、正下、右下的值
                int down = matrix[i + 1][j];
                int leftDown = j > 0 ? matrix[i + 1][j - 1] : Integer.MAX_VALUE;
                int rightDown = j < n - 1 ? matrix[i + 1][j + 1] : Integer.MAX_VALUE;

                matrix[i][j] += Math.min(down, Math.min(leftDown, rightDown));
            }
        }

        // 返回第一行中的最小值
        int result = Integer.MAX_VALUE;
        for (int val : matrix[0]) {
            result = Math.min(result, val);
        }
        return result;
    }

    public int minFallingPathSumOptim(int[][] matrix) {
        int n = matrix.length;
        int[][] dp = new int[n][n];

        // 初始化最后一行：从原 matrix 复制
        for (int j = 0; j < n; j++) {
            dp[n - 1][j] = matrix[n - 1][j];
        }

        // 自底向上填充 dp 数组
        for (int i = n - 2; i >= 0; i--) {
            for (int j = 0; j < n; j++) {
                int down = dp[i + 1][j];
                int leftDown = j > 0 ? dp[i + 1][j - 1] : Integer.MAX_VALUE;
                int rightDown = j < n - 1 ? dp[i + 1][j + 1] : Integer.MAX_VALUE;

                dp[i][j] = matrix[i][j] + Math.min(down, Math.min(leftDown, rightDown));
            }
        }

        // 第一行中最小的就是答案
        int result = Integer.MAX_VALUE;
        for (int j = 0; j < n; j++) {
            result = Math.min(result, dp[0][j]);
        }

        return result;
    }

    public int minFallingPathSumOptimOptim(int[][] matrix) {
        int n = matrix.length;
        // 初始化 prev 表示下一行（从最后一行开始）
        int[] prev = new int[n];
        for (int j = 0; j < n; j++) {
            prev[j] = matrix[n - 1][j];
        }

        // 从倒数第二行开始往上计算
        for (int i = n - 2; i >= 0; i--) {
            int[] curr = new int[n];
            for (int j = 0; j < n; j++) {
                int down = prev[j];
                int leftDown = j > 0 ? prev[j - 1] : Integer.MAX_VALUE;
                int rightDown = j < n - 1 ? prev[j + 1] : Integer.MAX_VALUE;

                curr[j] = matrix[i][j] + Math.min(down, Math.min(leftDown, rightDown));
            }
            // 当前行计算完后变成下一轮的 prev
            prev = curr;
        }

        // prev 是第一行的结果，取最小值
        int result = Integer.MAX_VALUE;
        for (int val : prev) {
            result = Math.min(result, val);
        }

        return result;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        int[][][] testCases = {
            {
                {2, 1, 3},
                {6, 5, 4},
                {7, 8, 9}
            },
            {
                {-19, 57},
                {-40, -5}
            },
            {
                {1}
            },
            {
                {1, 2},
                {3, 4}
            },
            {
                {100, 100},
                {100, 100}
            },
            {
                {-1, -2, -3},
                {-4, -5, -6},
                {-7, -8, -9}
            },
            {
                {10, 10, 1},
                {1, 1, 10},
                {10, 1, 10}
            }
        };

        int[] expectedResults = {
            13,      // 1 -> 4 -> 8
            -59,     // -19 -> -40
            1,
            3,       // 1 -> 2
            200,     // 100 -> 100
            -15,     // -3 -> -6 -> -6
            3        // 1 -> 1 -> 1
        };

        for (int i = 0; i < testCases.length; i++) {
            int[][] matrix = deepCopy(testCases[i]);
            int expected = expectedResults[i];

            int result1 = solution.minFallingPathSum(deepCopy(matrix));
            int result2 = solution.minFallingPathSumOptim(deepCopy(matrix));
            int result3 = solution.minFallingPathSumOptimOptim(deepCopy(matrix));

            System.out.println("Test case " + (i + 1) + ": matrix = " + Arrays.deepToString(matrix));
            System.out.println("Expected: " + expected);

            System.out.println("  minFallingPathSum       = " + result1 + (result1 == expected ? " ✅ Pass" : " ❌ Fail"));
            System.out.println("  minFallingPathSumOptim  = " + result2 + (result2 == expected ? " ✅ Pass" : " ❌ Fail"));
            System.out.println("  minFallingPathSumOptimOptim = " + result3 + (result3 == expected ? " ✅ Pass" : " ❌ Fail"));
            System.out.println("------------------------------------------------");
        }
    }

    // 辅助函数：复制二维数组，避免原地修改影响其他测试
    private static int[][] deepCopy(int[][] original) {
        if (original == null) return null;
        int[][] copy = new int[original.length][];
        for (int i = 0; i < original.length; i++) {
            copy[i] = Arrays.copyOf(original[i], original[i].length);
        }
        return copy;
    }
}