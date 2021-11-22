class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
       if fast:
            slow = slow.next

            
                
        def reverse(head):
            temp = None
            prev = None
            while head:
                temp = head.next
                head.next = prev
                prev = head
                head = temp
            return prev
 


        
        slow = reverse(slow)
        while slow:
            if head.val != slow.val:
                return False
            head = head.next
            slow = slow.next
        return True
