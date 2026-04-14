# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        list_map = {}
        idx = 0
        while head:
            list_map[idx] = head
            head = head.next
            idx += 1

        dummy = ListNode()
        curr = dummy
        l, r = 0, len(list_map.keys()) - 1
        while l <= r:
            curr.next = list_map[l]
            curr = curr.next
            curr.next = list_map[r]
            curr = curr.next
            l += 1
            r -= 1
        curr.next = None
        
        