/*
 * 给你单链表的头结点 head ，请你找出并返回链表的中间结点。
 * 如果有两个中间结点，则返回第二个中间结点。  
 */

class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}

class Solution {
    public ListNode middleNode(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        return slow;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        int[][] testCases = {
            {1, 2, 3, 4, 5},       
            {1, 2, 3, 4, 5, 6},   
            {1},                   
            {},                   
        };

        int[] expectedResults = {3, 4, 1, -1};

        for (int i = 0; i < testCases.length; i++) {
            int[] arr = testCases[i];
            ListNode head = createLinkedList(arr);
            ListNode middle = solution.middleNode(head);

            int actual = (middle != null) ? middle.val : -1;

            System.out.print("Test case " + (i + 1) + ": ");
            System.out.print("Input = " + arrayToString(arr));
            System.out.print(", Expected = " + expectedResults[i]);
            System.out.println(", Actual = " + actual + (expectedResults[i] == actual ? " ✅ Pass" : " ❌ Fail"));
        }
    }

    private static ListNode createLinkedList(int[] arr) {
        if (arr.length == 0) return null;
        ListNode head = new ListNode(arr[0]);
        ListNode current = head;
        for (int i = 1; i < arr.length; i++) {
            current.next = new ListNode(arr[i]);
            current = current.next;
        }
        return head;
    }

    private static String arrayToString(int[] arr) {
        if (arr.length == 0) return "[]";
        StringBuilder sb = new StringBuilder("[");
        for (int val : arr) {
            sb.append(val).append(", ");
        }
        sb.setLength(sb.length() - 2);
        sb.append("]");
        return sb.toString();
    }
}
