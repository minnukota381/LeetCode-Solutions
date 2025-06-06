# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        c=head
        while c and c.next:
            if c.val == c.next.val:
                c.next=c.next.next
            else:
                c=c.next
        return head
        