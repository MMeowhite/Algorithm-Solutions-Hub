"""
给你单链表的头结点 head ，请你找出并返回链表的中间结点。
如果有两个中间结点，则返回第二个中间结点。
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
def list_to_linkedlist(lst):
    if not lst:
        return None
    dummy = ListNode()
    cur = dummy
    for v in lst:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next

def linkedlist_to_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res

def test():
    sol = Solution()
    test_cases = [
        ([1, 2, 3, 4, 5], [3, 4, 5]),    
        ([1, 2, 3, 4, 5, 6], [4, 5, 6]), 
        ([1], [1]),                      
        ([], []),                      
        ([1, 2], [2])                   
    ]

    for i, (input_list, expected_list) in enumerate(test_cases):
        head = list_to_linkedlist(input_list)
        middle = sol.middleNode(head)
        result_list = linkedlist_to_list(middle)
        print(f"Test case {i+1}: input = {input_list}")
        print(f"Expected middle node list: {expected_list}")
        print(f"Got:                     {result_list}")
        print("Pass ✅" if result_list == expected_list else "Fail ❌")
        print("-" * 40)

if __name__ == "__main__":
    test()
