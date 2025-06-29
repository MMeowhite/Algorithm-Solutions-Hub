/*
 * 给你两个字符串：ransomNote 和 magazine ，判断 ransomNote 能不能由 magazine 里面的字符构成。
 * 如果可以，返回 true ；否则返回 false 。
 * magazine 中的每个字符只能在 ransomNote 中使用一次。
 */

class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        int[] counts = new int[26];  // 用于记录 magazine 中每个字母的出现次数

        for (char c : magazine.toCharArray()) {
            counts[c - 'a']++;  // 累加 magazine 中的字符
        }

        for (char c : ransomNote.toCharArray()) {
            counts[c - 'a']--;  // 使用一个字符
            if (counts[c - 'a'] < 0) {
                return false;  // 某个字符不足
            }
        }

        return true;  // 所有字符都有足够数量
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        String[][] testCases = {
            { "a", "b" },         
            { "aa", "ab" },       
            { "aa", "aab" },      
            { "abc", "aabbcc" },  
            { "abc", "def" },     
            { "", "anything" },   
            { "a", "a" },         
            { "aaa", "aa" }       
        };

        boolean[] expectedResults = {
            false, false, true, true, false, true, true, false
        };

        for (int i = 0; i < testCases.length; i++) {
            String ransomNote = testCases[i][0];
            String magazine = testCases[i][1];
            boolean expected = expectedResults[i];
            boolean actual = solution.canConstruct(ransomNote, magazine);

            System.out.print("Test case " + (i + 1) + ": ");
            System.out.print("ransomNote = \"" + ransomNote + "\", magazine = \"" + magazine + "\"");
            System.out.print(", Expected = " + expected);
            System.out.println(", Actual = " + actual + (expected == actual ? " ✅ Pass" : " ❌ Fail"));
        }
    }
}
