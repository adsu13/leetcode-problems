class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        return f"ListNode({self.val}, {self.next})"
    
    @classmethod
    def deserialize(cls, data):
        if not data:
            return None
        head = ListNode(data[0])
        current = head
        for val in data[1:]:
            current.next = ListNode(val)
            current = current.next
        return head
    
    def serialize(self):
        result = []
        current = self
        while current:
            result.append(current.val)
            current = current.next
        return result

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10
            
            current.next = ListNode(digit)
            current = current.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next.serialize() 