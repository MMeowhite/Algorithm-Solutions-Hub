/*
 * 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
 * 请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。
 */

import java.util.*;

class Solution {
    public int[][] merge(int[][] intervals) {
        if (intervals == null || intervals.length == 0) {
            return new int[0][0];
        }

        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));

        List<int[]> merged = new ArrayList<>();

        for (int[] interval : intervals) {
            if (merged.isEmpty() || merged.get(merged.size() - 1)[1] < interval[0]) {
                merged.add(interval);
            } else {
                merged.get(merged.size() - 1)[1] = Math.max(merged.get(merged.size() - 1)[1], interval[1]);
            }

        }

        return merged.toArray(new int[merged.size()][]);
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        int[][][] testCases = {
                { { 1, 3 }, { 2, 6 }, { 8, 10 }, { 15, 18 } }, // 期望 [[1,6],[8,10],[15,18]]
                { { 1, 4 }, { 4, 5 } }, // 期望 [[1,5]]
                { { 1, 4 }, { 0, 2 }, { 3, 5 } }, // 期望 [[0,5]]
                { { 1, 4 } }, // 期望 [[1,4]]
                {} // 空输入，期望 []
        };

        int[][][] expected = {
                { { 1, 6 }, { 8, 10 }, { 15, 18 } },
                { { 1, 5 } },
                { { 0, 5 } },
                { { 1, 4 } },
                {}
        };

        for (int i = 0; i < testCases.length; i++) {
            int[][] result = solution.merge(testCases[i]);
            System.out.println("Test case " + (i + 1) + ":");
            System.out.println("Input:    " + java.util.Arrays.deepToString(testCases[i]));
            System.out.println("Expected: " + java.util.Arrays.deepToString(expected[i]));
            System.out.println("Result:   " + java.util.Arrays.deepToString(result));
            boolean pass = java.util.Arrays.deepEquals(result, expected[i]);
            System.out.println(pass ? "✅ Pass" : "❌ Fail");
            System.out.println("--------------------------------------------------");
        }
    }
}