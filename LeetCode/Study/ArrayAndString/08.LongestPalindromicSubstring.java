/*
 * 给你一个字符串 s，找到 s 中最长的 回文 子串。
 */
import java.util.Arrays;
import java.util.List;

class Solution {
    public String longestPalindrome(String s){
        if (s == null || s.length() < 1) return "";

        int start = 0, end = 0;
        for (int i = 0; i < s.length(); i++) {
            int len1 = expandAroundCenter(s, i, i); // odd length
            int len2 = expandAroundCenter(s, i, i + 1); // even length
            int len = Math.max(len1, len2);

            if (len > end - start) {
                start = i - (len - 1) / 2;
                end  = i + len / 2;
            }
        }

        return s.substring(start, end + 1);
    }

    private int expandAroundCenter(String s, int left, int right) {
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }

        return right - left - 1;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        
        Object[][] testCases = {
            {"babad", Arrays.asList("bab", "aba")},  // Multiple valid answers
            {"cbbd", "bb"},
            {"a", "a"},
            {"ac", "a"},  // or "c" - both are valid
            {"racecar", "racecar"},
            {"", ""},
            {"abb", "bb"}
        };
        
        for (int i = 0; i < testCases.length; i++) {
            String input = (String) testCases[i][0];
            Object expected = testCases[i][1];
            
            String result = sol.longestPalindrome(input);
            
            System.out.println("Test case " + (i + 1) + ":");
            System.out.println("Input:    " + input);
            System.out.println("Expected: " + expected);
            System.out.println("Result:   " + result);
            
            if (expected instanceof List) {
                System.out.println(((List<String>) expected).contains(result) ? "✅ Pass" : "❌ Fail");
            } else {
                System.out.println(expected.equals(result) ? "✅ Pass" : "❌ Fail");
            }
            System.out.println("-".repeat(40));
        }
    }
}
