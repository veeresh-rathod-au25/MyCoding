class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
            lst=[]
            temp=head
            while temp:
                lst.append(str(temp.val))
                temp=temp.next
            print(lst)
            s="".join(lst)
            ans=int(s,2)
            return ans