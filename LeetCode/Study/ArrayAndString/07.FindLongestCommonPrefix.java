/*
 * 编写一个函数来查找字符串数组中的最长公共前缀。
 * 如果不存在公共前缀，返回空字符串 ""。
 */

import java.util.Arrays;

class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0 || strs == null) {
            return "";
        }

        String base = strs[0];

        for (int i = 0; i < base.length(); i++) {
            char c= base.charAt(i);
            for (int j = 0; j < strs.length; j++) {
                if (i >= strs[j].length() || strs[j].charAt(i) != c){
                    return base.substring(0, i);
                }
            }
        }

        return base;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        
        Object[][] testCases = {
            {new String[]{"flower", "flow", "flight"}, "fl"},
            {new String[]{"dog", "racecar", "car"}, ""},
            {new String[]{"a"}, "a"},
            {new String[]{"", ""}, ""},
            {new String[]{}, ""},
            {new String[]{"apple", "appetite", "application"}, "app"},
            {new String[]{"same", "same", "same"}, "same"},
            {new String[]{"prefix", "preface", "premium"}, "pre"}
        };
        
        for (int i = 0; i < testCases.length; i++) {
            String[] input = (String[]) testCases[i][0];
            String expected = (String) testCases[i][1];
            
            String result = sol.longestCommonPrefix(input);
            
            System.out.println("Test case " + (i + 1) + ":");
            System.out.println("Input:    " + Arrays.toString(input));
            System.out.println("Expected: " + expected);
            System.out.println("Result:   " + result);
            System.out.println(result.equals(expected) ? "✅ Pass" : "❌ Fail");
            System.out.println("-".repeat(40));
        }
    }
}