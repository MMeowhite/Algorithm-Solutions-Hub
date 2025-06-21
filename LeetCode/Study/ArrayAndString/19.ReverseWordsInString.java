/*
 * 给定一个字符串 s ，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
 */

class Solution {
    public String reverseWords(String s) {
        String[] words = s.trim().split("\\s+"); // 去掉首尾空格并按多个空格分词
        StringBuilder result = new StringBuilder();

        for (int i = 0; i < words.length; i++) {
            result.append(new StringBuilder(words[i]).reverse());
            if (i < words.length - 1) {
                result.append(' ');
            }
        }

        return result.toString();
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        String[] testInputs = {
            "Let's take LeetCode contest",  // 基本句子
            "  hello   world  ",            // 多个空格
            "a",                            // 单字母
            "  a b  c ",                    // 多个空格
            "",                             // 空字符串
            "123 456 789",                  // 数字串
            "你好 世界",                    // 中文（或其他非拉丁字母）
            "word1, word2!",               // 含标点
            "    ",                         // 全是空格
            "Hi! Are you okay?",            // 问句 + 标点
            "mixedCASE and lowercase",      // 大小写测试
        };

        String[] expectedOutputs = {
            "s'teL ekat edoCteeL tsetnoc",
            "olleh dlrow",
            "a",
            "a b c",
            "",
            "321 654 987",
            "好你 界世",
            "1drow, 2drow!",
            "",
            "!iH erA uoy ?yako",
            "ESACdexim dna esacrewol"
        };

        for (int i = 0; i < testInputs.length; i++) {
            String input = testInputs[i];
            String expected = expectedOutputs[i];
            String result = sol.reverseWords(input);

            System.out.println("Test case " + (i + 1) + ":");
            System.out.println("Input: \"" + input + "\"");
            System.out.println("Expected: \"" + expected + "\"");
            System.out.println("Result:   \"" + result + "\"");
            System.out.println(expected.equals(result) ? "✅ Pass" : "❌ Fail");
            System.out.println("----------------------------------------");
        }
    }
}