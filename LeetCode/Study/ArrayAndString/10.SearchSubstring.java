class Solution {
    public int strStr(String haystack, String needle) {
        if (needle.isEmpty()) return 0;
        int n = haystack.length(), m = needle.length();
        if (m > n) return -1;

        for (int i = 0; i < n - m; i++) {
            int j;
            for (j = 0; j < m; j++) {
                if (haystack.charAt(i + i) != needle.charAt(j)){
                    break;
                }
            }
            if (j == m) return i;
        }
        return -1;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        String[][] testCases = {
            {"hello", "ll", "2"},
            {"aaaaa", "bba", "-1"},
            {"", "", "0"},
            {"abc", "c", "2"},
            {"mississippi", "issip", "4"},
            {"a", "a", "0"},
            {"abc", "abcd", "-1"},
            {"aabaaabaaac", "aabaaac", "4"}
        };
        
        for (int i = 0; i < testCases.length; i++) {
            String h = testCases[i][0];
            String n = testCases[i][1];
            int exp = Integer.parseInt(testCases[i][2]);
            int res = sol.strStr(h, n);
            
            System.out.printf("Test %d: h='%s', n='%s'\n", i+1, h, n);
            System.out.printf("Expected: %d, Result: %d\n", exp, res);
            System.out.println(res == exp ? "✅ Pass" : "❌ Fail");
            System.out.println("-".repeat(40));
        }
    }
}
