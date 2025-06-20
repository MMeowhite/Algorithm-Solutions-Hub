/*
 * 编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 s 的形式给出。
 * 不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
 */

import java.util.Arrays;

class Solution {
    public void reverseString(char[] s) {
        int left = 0;
        int right = s.length - 1;
        
        while (left < right) {
            char temp = s[left];
            s[left] = s[right];
            s[right] = temp;
            left++;
            right--;
        }
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        // 用二维数组表示多个测试用例，输入字符数组以及期望的输出
        Object[][] testCases = {
            {new char[]{'h', 'e', 'l', 'l', 'o'}, new char[]{'o', 'l', 'l', 'e', 'h'}},
            {new char[]{'H', 'a', 'n', 'n', 'a', 'h'}, new char[]{'h', 'a', 'n', 'n', 'a', 'H'}},
            {new char[]{'a', 'b', 'c'}, new char[]{'c', 'b', 'a'}},
            {new char[]{'a'}, new char[]{'a'}}, // 单一字符，反转后应该还是原来
            {new char[]{}, new char[]{}} // 空字符数组
        };

        for (int i = 0; i < testCases.length; i++) {
            char[] input = (char[]) testCases[i][0];
            char[] expected = (char[]) testCases[i][1];
            sol.reverseString(input);

            System.out.printf("Test %d: input=%s\n", i + 1, new String(input));
            System.out.printf("Expected: %s, Result: %s\n", new String(expected), new String(input));
            boolean passed = Arrays.equals(input, expected);
            System.out.println(passed ? "✅ Pass" : "❌ Fail");
            System.out.println("-".repeat(40));
        }
    }
}
