/*
 * 给你一个 m x n 的整数网格 accounts ，其中 accounts[i][j] 是第 i​​​​​​​​​​​​ 位客户在第 j 家银行托管的资产数量。返回最富有客户所拥有的 资产总量 。
 * 客户的 资产总量 就是他们在各家银行托管的资产数量之和。最富有客户就是 资产总量 最大的客户。
 */

import java.util.Arrays;

class Solution {
    public int maximumWealth(int[][] accounts) {
        int max_wealth = 0;

        for(int i = 0; i < accounts.length; i++){
            int wealth = 0;
            for (int j = 0; j < accounts[0].length; j++){
                wealth += accounts[i][j];
            }

            if (max_wealth < wealth) {
                max_wealth = wealth;
            }
        }

        return max_wealth;

        // solution with one line code
        // return Arrays.stream(accounts).map(Arrays::stream).mapToInt(IntStream::sum).reduce(0, Math::max);
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        int[][][] testCases = {
            { {1, 2, 3}, {3, 2, 1} },         // 6
            { {1, 5}, {7, 3}, {3, 5} },       // 10
            { {2, 8, 7}, {7, 1, 3}, {1, 9, 5} }, // 17
            { {0, 0, 0} },                    // 0
            { {} }                           // 0，空数组的情况
        };

        int[] expectedResults = {6, 10, 17, 0, 0};

        for (int i = 0; i < testCases.length; i++) {
            int actual = solution.maximumWealth(testCases[i]);
            System.out.print("Test case " + (i + 1) + ": ");
            System.out.print("Input = " + Arrays.deepToString(testCases[i]));
            System.out.print(", Expected = " + expectedResults[i]);
            System.out.println(", Actual = " + actual + (actual == expectedResults[i] ? " ✅ Pass" : " ❌ Fail"));
        }
    }
}
