/*
 * 编写一种算法，若M × N矩阵中某个元素为0，则将其所在的行与列清零。
 */

import java.util.Arrays;

class Solution {
    public void setZeroes(int[][] matrix) {
        int m = matrix.length;
        if (m == 0) return;
        int n = matrix[0].length;

        boolean[] rows = new boolean[m];
        boolean[] cols = new boolean[n];

        // 记录需要置零的行和列
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == 0) {
                    rows[i] = true;
                    cols[j] = true;
                }
            }
        }

        // 置零对应行
        for (int i = 0; i < m; i++) {
            if (rows[i]) {
                for (int j = 0; j < n; j++) {
                    matrix[i][j] = 0;
                }
            }
        }

        // 置零对应列
        for (int j = 0; j < n; j++) {
            if (cols[j]) {
                for (int i = 0; i < m; i++) {
                    matrix[i][j] = 0;
                }
            }
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        int[][][] testCases = {
            { {1, 1, 1}, {1, 0, 1}, {1, 1, 1} },
            { {0, 1, 2, 0}, {3, 4, 5, 2}, {1, 3, 1, 5} },
            { {1} },
            { {0} },
            {}
        };

        int[][][] expected = {
            { {1, 0, 1}, {0, 0, 0}, {1, 0, 1} },
            { {0, 0, 0, 0}, {0, 4, 5, 0}, {0, 3, 1, 0} },
            { {1} },
            { {0} },
            {}
        };

        for (int i = 0; i < testCases.length; i++) {
            System.out.println("Test case " + (i + 1) + ":");
            System.out.println("Input:    " + Arrays.deepToString(testCases[i]));

            if (testCases[i].length > 0) {
                solution.setZeroes(testCases[i]);
            }

            System.out.println("Expected: " + Arrays.deepToString(expected[i]));
            System.out.println("Result:   " + Arrays.deepToString(testCases[i]));
            boolean pass = Arrays.deepEquals(testCases[i], expected[i]);
            System.out.println(pass ? "✅ Pass" : "❌ Fail");
            System.out.println("--------------------------------------------------");
        }
    }
}
