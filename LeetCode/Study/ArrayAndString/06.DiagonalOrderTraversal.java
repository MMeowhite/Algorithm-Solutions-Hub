/*
 * 给你一个大小为 m x n 的矩阵 mat ，请以对角线遍历的顺序，用一个数组返回这个矩阵中的所有元素。
 */


import java.util.*;

class Solution {
    public int[] findDiagonalOrder(int[][] mat) {
        int n = mat.length;
        if (n == 0) return new int[0];
        int m = mat[0].length;

        int[] result = new int[n * m];
        int index = 0;

        for (int s = 0; s < n + m - 2; s++) {
            // 临时存放堆钱对角线的元素
            List<Integer> intermediate = new ArrayList<>();

            int startRow = Math.max(0, s - m + 1);
            int endRow = Math.min(s, n - 1);

            for (int i = startRow; i < endRow; i++) {
                int j = s - i;
                intermediate.add(mat[i][j]);
            }

            if (s % 2 == 0) {
                Collections.reverse(intermediate);
            }

            for (int num : intermediate) {
                result[index++] = num;
            }
        }

        return result;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        int[][][] testCases = {
            { {1, 2, 3}, {4, 5, 6}, {7, 8, 9} },
            { {1, 2}, {3, 4} },
            { {1} },
            { {} },
            {}
        };

        int[][] expectedResults = {
            {1, 2, 4, 7, 5, 3, 6, 8, 9},
            {1, 2, 3, 4},
            {1},
            {},
            {}
        };

        for (int i = 0; i < testCases.length; i++) {
            int[] result = sol.findDiagonalOrder(testCases[i]);
            System.out.println("Test case " + (i + 1) + ":");
            System.out.println("Input:    " + Arrays.deepToString(testCases[i]));
            System.out.println("Expected: " + Arrays.toString(expectedResults[i]));
            System.out.println("Result:   " + Arrays.toString(result));
            boolean pass = Arrays.equals(result, expectedResults[i]);
            System.out.println(pass ? "✅ Pass" : "❌ Fail");
            System.out.println("--------------------------------------------------");
        }
    }
}
