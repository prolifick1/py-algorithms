"""
Leetcode(https://leetcode.com/problems/reverse-linked-list)
Get the head of a singly linked list,
reverse the list, and return the head of the reversed list.
"""

# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# O(n) Time | O(1) Space
def reverse_linked_list(head):
    prevNode = None
    nextNode = head
    while head:
        nextNode = head.next
        head.next = prevNode
        prevNode = head
        head = nextNode
    return prevNode

#head = ListNode(1)
#second = ListNode(2)
#third = ListNode(3) 
#head.next = second
#second.next = third
#
#reverse_linked_list(head)
