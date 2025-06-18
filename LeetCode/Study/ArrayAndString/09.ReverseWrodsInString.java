/*
 * 给你一个字符串 s ，请你反转字符串中 单词 的顺序。
 * 单词 是由非空格字符组成的字符串。s 中使用至少一个空格将字符串中的 单词 分隔开。
 * 返回 单词 顺序颠倒且 单词 之间用单个空格连接的结果字符串。
 * 注意：输入字符串 s中可能会存在前导空格、尾随空格或者单词间的多个空格。返回的结果字符串中，单词间应当仅用单个空格分隔，且不包含任何额外的空格。
 */

import java.util.*;

class Solution {
    public String reverseWords(String s) {
        String[] words = s.trim().split("\\s+");
        StringBuilder sb = new StringBuilder();

        for (int i = words.length - 1; i >= 0 ; i--) {
            sb.append(words[i]);
            if (i > 0) sb.append(" ");
        }

        return sb.toString();
    }

    public String reverseWordsWithCollections(String s) {
        // 1. 去除首尾空格
        s = s.trim();
        // 2. 分割单词（正则表达式匹配一个或多个空格）
        List<String> words = Arrays.asList(s.split("\\s+"));
        // 3. 反转单词列表
        Collections.reverse(words);
        // 4. 用单个空格连接单词
        return String.join(" ", words);
    }

    private void testReverseWordsFunction(String methodName) {
        System.out.println("\nTesting method: " + methodName);
        
        String[][] testCases = {
            {"the sky is blue", "blue is sky the"},
            {"  hello world  ", "world hello"},
            {"a good   example", "example good a"},
            {"  Bob    Loves  Alice   ", "Alice Loves Bob"},
            {"Alice does not even like bob", "bob like even not does Alice"},
            {"", ""},
            {"   ", ""},
            {"single", "single"},
            {"  a  b  c  ", "c b a"},
            {"!@# $% ^&*", "^&* $% !@#"},
            {"  multiple    spaces   between   words  ", "words between spaces multiple"}
        };

        int passed = 0;
        for (int i = 0; i < testCases.length; i++) {
            String input = testCases[i][0];
            String expected = testCases[i][1];
            String result;
            
            if (methodName.equals("reverseWords")) {
                result = reverseWords(input);
            } else {
                result = reverseWordsWithCollections(input);
            }

            boolean isCorrect = result.equals(expected);
            if (isCorrect) passed++;

            System.out.println("Test case " + (i + 1) + ":");
            System.out.println("Input:    \"" + input + "\"");
            System.out.println("Expected: \"" + expected + "\"");
            System.out.println("Result:   \"" + result + "\"");
            System.out.println(isCorrect ? "✅ Pass" : "❌ Fail");
            System.out.println("-".repeat(60));
        }
        
        System.out.printf("Test summary: %d/%d passed (%.1f%%)%n",
                         passed, testCases.length, (passed * 100.0 / testCases.length));
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        
        // 测试第一个方法
        sol.testReverseWordsFunction("reverseWords");
        
        // 测试第二个方法
        sol.testReverseWordsFunction("reverseWordsWithCollections");
    }

}