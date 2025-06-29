/*
 * 给你一个非负整数 num ，请你返回将它变成 0 所需要的步数。 如果当前数字是偶数，你需要把它除以 2 ；否则，减去 1 。
 */


class Solution {
    public int numberOfSteps(int num) {
        int count = 0;

        while (num > 0) {
            if (num % 2 == 0){
                num = num / 2;
            } else {
                num--;
            }
            count++;
        }

        return count;
            
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        int[] testCases = {14, 8, 123, 0, 1};
        int[] expectedResults = {6, 4, 12, 0, 1};

        for (int i = 0; i < testCases.length; i++) {
            int input = testCases[i];
            int expected = expectedResults[i];
            int actual = solution.numberOfSteps(input);

            System.out.print("Test case " + (i + 1) + ": Input = " + input);
            System.out.print(", Expected = " + expected);
            System.out.println(", Actual = " + actual + (expected == actual ? " ✅ Pass" : " ❌ Fail"));
        }
    }
}
