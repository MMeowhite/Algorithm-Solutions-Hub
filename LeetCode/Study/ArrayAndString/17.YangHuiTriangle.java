/*
 * 给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。
 * 在「杨辉三角」中，每个数是它左上方和右上方的数的和。
 */

import java.util.List;
import java.util.ArrayList;


 class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> triangle = new ArrayList<>();

        for (int i = 0; i < numRows; i++) {
            List<Integer> row = new ArrayList<>();
            
            for (int j = 0; j <= i; j++) {
                // 每一行的开头和结尾都是 1
                if (j == 0 || j == i) {
                    row.add(1);
                } else {
                    // 中间的值是上一行的两个相邻元素之和
                    int val = triangle.get(i - 1).get(j - 1) + triangle.get(i - 1).get(j);
                    row.add(val);
                }
            }

            triangle.add(row);
        }

        return triangle;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        int[] testInputs = {0, 1, 2, 3, 4, 5};
        List<List<List<Integer>>> expectedOutputs = List.of(
            List.of(),
            List.of(List.of(1)),
            List.of(List.of(1), List.of(1, 1)),
            List.of(List.of(1), List.of(1, 1), List.of(1, 2, 1)),
            List.of(List.of(1), List.of(1, 1), List.of(1, 2, 1), List.of(1, 3, 3, 1)),
            List.of(List.of(1), List.of(1, 1), List.of(1, 2, 1), List.of(1, 3, 3, 1), List.of(1, 4, 6, 4, 1))
        );

        for (int i = 0; i < testInputs.length; i++) {
            int numRows = testInputs[i];
            List<List<Integer>> expected = expectedOutputs.get(i);
            List<List<Integer>> result = sol.generate(numRows);

            System.out.println("Test case " + (i + 1) + ":");
            System.out.println("Input: " + numRows);
            System.out.println("Expected: " + expected);
            System.out.println("Result:   " + result);
            System.out.println(expected.equals(result) ? "✅ Pass" : "❌ Fail");
            System.out.println("----------------------------------------");
        }
    }
}