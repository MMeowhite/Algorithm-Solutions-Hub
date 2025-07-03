/*
 * 在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。
 */
package LeetCode.Study.DynamicProgramming;

import java.util.Arrays;

class Solution {
    public int maximalSquare(char[][] matrix) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) return 0;

        int rows = matrix.length;
        int cols = matrix[0].length;

        int maxLen = 0;
        int[][] dp = new int[rows][cols];

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                // 判断以位置 (i, j) 为右下角的最大正方形的边长是多少
                if (matrix[i][j] == '1') {
                    if (i == 0 || j == 0) {
                        dp[i][j] = 1;
                    } else {
                        dp[i][j] = Math.min(
                            Math.min(dp[i - 1][j], dp[i][j - 1]),
                            dp[i - 1][j - 1]
                        ) + 1;
                    }
                    maxLen = Math.max(maxLen, dp[i][j]);
                }
            }
        }

        return maxLen * maxLen;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        char[][][] testCases = {
            {
                {'1', '0', '1', '0', '0'},
                {'1', '0', '1', '1', '1'},
                {'1', '1', '1', '1', '1'},
                {'1', '0', '0', '1', '0'}
            },
            {
                {'0', '1'},
                {'1', '0'}
            },
            {
                {'0'}
            },
            {
                {'1'}
            },
            {
                {'1', '1', '1'},
                {'1', '1', '1'},
                {'1', '1', '1'}
            },
            {
                {'0', '0', '0'},
                {'0', '0', '0'},
                {'0', '0', '0'}
            },
            {
                {'1', '0', '1', '1'},
                {'1', '1', '1', '1'},
                {'1', '1', '1', '0'}
            }
        };

        int[] expectedResults = {
            4,  // 2x2 square
            1,  // only individual 1s
            0,  // no 1s
            1,  // single 1
            9,  // full 3x3 square
            0,  // all 0s
            4   // 2x2 square
        };

        for (int i = 0; i < testCases.length; i++) {
            char[][] matrix = testCases[i];
            int expected = expectedResults[i];
            int actual = solution.maximalSquare(matrix);

            System.out.println("Test case " + (i + 1) + ":");
            for (char[] row : matrix) {
                System.out.println("  " + Arrays.toString(row));
            }

            System.out.println("Expected: " + expected + ", Actual: " + actual +
                    (expected == actual ? " ✅ Pass" : " ❌ Fail"));
            System.out.println("---------------------------------------------------");
        }
    }
}