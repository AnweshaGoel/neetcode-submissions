# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        for i in range(1, len(lists)):
            lists[i] = self.merge(lists[i-1], lists[i])
        return lists[-1]
    
    def merge(self, one, two):
        dummy = ListNode()
        tail = dummy
        while one and two:
            if one.val <= two.val:
                tail.next = one
                one = one.next
            else:
                tail.next = two
                two = two.next
            tail = tail.next
        if one:
            tail.next = one
        if two:
            tail.next = two
        return dummy.next
        