/*
 * 给你一个整数 n ，返回一个字符串数组 answer（下标从 1 开始），其中：
 * answer[i] == "FizzBuzz" 如果 i 同时是 3 和 5 的倍数。
 * answer[i] == "Fizz" 如果 i 是 3 的倍数。
 * answer[i] == "Buzz" 如果 i 是 5 的倍数。
 * answer[i] == i （以字符串形式）如果上述条件全不满足。
 */
import java.util.*;

class Solution {
    public List<String> fizzBuzz(int n) {
        List<String> result = new ArrayList<>();

        for (int i = 1; i <= n; i++) {
            if (i % 3 == 0 && i % 5 == 0) {
                result.add("FizzBuzz");
            } else if (i % 3 == 0) {
                result.add("Fizz");
            } else if (i % 5 == 0) {
                result.add("Buzz");
            } else {
                result.add(String.valueOf(i)); 
            }
        }

        return result;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        int[] testInputs = { 1, 3, 5, 15 };
        List<List<String>> expectedOutputs = List.of(
            List.of("1"),
            List.of("1", "2", "Fizz"),
            List.of("1", "2", "Fizz", "4", "Buzz"),
            List.of("1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz")
        );

        for (int i = 0; i < testInputs.length; i++) {
            int input = testInputs[i];
            List<String> expected = expectedOutputs.get(i);
            List<String> actual = solution.fizzBuzz(input);

            System.out.print("Test case " + (i + 1) + ": n = " + input);
            boolean passed = expected.equals(actual);
            System.out.println(passed ? " ✅ Pass" : " ❌ Fail");
            if (!passed) {
                System.out.println("  Expected: " + expected);
                System.out.println("  Actual:   " + actual);
            }
        }
    }
}