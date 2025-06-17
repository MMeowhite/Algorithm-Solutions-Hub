/*
 * 给你一幅由 N × N 矩阵表示的图像，其中每个像素的大小为 4 字节。请你设计一种算法，将图像旋转 90 度。
 * 不占用额外内存空间能否做到？
 */

import java.util.Arrays;

class Solution {
    public void rotate(int[][] matrix) {
        int n = matrix.length;
        if (n == 0) return;

        // 转置
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }

        // 反转每一行
        for (int i = 0; i < n; i++) {
            int left = 0, right = n - 1;
            while (left < right) {
                int temp = matrix[i][left];
                matrix[i][left] = matrix[i][right];
                matrix[i][right] = temp;
                left++;
                right--;
            }
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        int[][][] testCases = {
            { {1, 2, 3}, {4, 5, 6}, {7, 8, 9} },
            { {5, 1, 9, 11}, {2, 4, 8, 10}, {13, 3, 6, 7}, {15, 14, 12, 16} },
            { {1} },
            {}
        };

        int[][][] expected = {
            { {7, 4, 1}, {8, 5, 2}, {9, 6, 3} },
            { {15, 13, 2, 5}, {14, 3, 4, 1}, {12, 6, 8, 9}, {16, 7, 10, 11} },
            { {1} },
            {}
        };

        for (int i = 0; i < testCases.length; i++) {
            System.out.println("Test case " + (i + 1) + ":");
            System.out.println("Input:    " + Arrays.deepToString(testCases[i]));

            if (testCases[i].length > 0) {
                solution.rotate(testCases[i]);
            }

            System.out.println("Expected: " + Arrays.deepToString(expected[i]));
            System.out.println("Result:   " + Arrays.deepToString(testCases[i]));
            boolean pass = Arrays.deepEquals(testCases[i], expected[i]);
            System.out.println(pass ? "✅ Pass" : "❌ Fail");
            System.out.println("--------------------------------------------------");
        }
    }
}
