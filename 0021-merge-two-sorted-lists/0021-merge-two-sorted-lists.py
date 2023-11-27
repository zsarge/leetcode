# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        if list1.val < list2.val:
            head = ListNode(list1.val)
            list1 = list1.next
        else:
            head = ListNode(list2.val)
            list2 = list2.next
        
        current = head
        def append(element: ListNode):
            nonlocal current
            current.next = element
            current = element
        
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                append(list1)
                list1 = list1.next
            else:
                append(list2)
                list2 = list2.next

        while list1 is not None:
            append(list1)
            list1 = list1.next

        while list2 is not None:
            append(list2)
            list2 = list2.next

        return head
