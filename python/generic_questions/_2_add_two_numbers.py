class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        while l1 is not None or l2 is not None or carry != 0:
            l1_val = l1.val if l1 is not None else 0
            l2_val = l2.val if l2 is not None else 0
            total = l1_val + l2_val + carry
            carry = total // 10
            digit = total % 10
            current.next = ListNode(digit)
            current = current.next
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        
        return dummy_head.next