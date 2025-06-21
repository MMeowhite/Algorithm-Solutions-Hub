/*
 * 给定一个非负索引 rowIndex，返回「杨辉三角」的第 rowIndex 行。
 * 在「杨辉三角」中，每个数是它左上方和右上方的数的和。
 */


import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> row = new ArrayList<>();
        row.add(1); // 第一行的第一个元素是 1
        for (int i = 1; i <= rowIndex; i++) {
            // 从后向前更新行，避免覆盖前一个元素
            for (int j = i - 1; j > 0; j--) {
                row.set(j, row.get(j) + row.get(j - 1));
            }
            // 添加新的元素到行的末尾
            row.add(1);
        }
        return row;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        int[] testInputs = {0, 1, 2, 3, 4, 5};
        List<List<Integer>> expectedOutputs = List.of(
            List.of(1),
            List.of(1, 1),
            List.of(1, 2, 1),
            List.of(1, 3, 3, 1),
            List.of(1, 4, 6, 4, 1),
            List.of(1, 5, 10, 10, 5, 1)
        );

        for (int i = 0; i < testInputs.length; i++) {
            int rowIndex = testInputs[i];
            List<Integer> expected = expectedOutputs.get(i);
            List<Integer> result = sol.getRow(rowIndex);

            System.out.println("Test case " + (i + 1) + ":");
            System.out.println("Input: " + rowIndex);
            System.out.println("Expected: " + expected);
            System.out.println("Result:   " + result);
            System.out.println(expected.equals(result) ? "✅ Pass" : "❌ Fail");
            System.out.println("----------------------------------------");
        }
    }
}