import unittest


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
def reverseLinkedList(head):
    prevNode = None
    nextNode = head
    while head:
        nextNode = head.next
        head.next = prevNode
        prevNode = head
        head = nextNode
    return prevNode


# For testing
# construct a linked list according to a list of values
def arrayToLinkedList(values=[]):
    head = None
    cur = None
    for i, val in enumerate(values):
        if i == 0:
            head = ListNode(val, None)
            cur = head
        else:
            cur.next = ListNode(val)
            cur = cur.next
    return head


# For testing
# obtain the list of values for the linked list
def linkedListToArray(head):
    res = []
    while head:
        if head.val != None:
            res.append(head.val)
            head = head.next
    return res


class MyTestCase(unittest.TestCase):
    def test1(self):
        nums = [1, 2, 3, 4, 5]
        head = arrayToLinkedList(nums)
        newHead = reverseLinkedList(head)
        values = linkedListToArray(newHead)
        nums.reverse()
        self.assertEqual(values, nums)

    def test2(self):
        nums = []
        head = arrayToLinkedList(nums)
        newHead = reverseLinkedList(head)
        values = linkedListToArray(newHead)
        nums.reverse()
        self.assertEqual(values, nums)

    def test3(self):
        nums = [1]
        head = arrayToLinkedList(nums)
        newHead = reverseLinkedList(head)
        values = linkedListToArray(newHead)
        nums.reverse()
        self.assertEqual(values, nums)

    def test4(self):
        myList = arrayToLinkedList([1, 2])
        reversedList = reverseLinkedList(myList);
        self.assertEqual(linkedListToArray(reversedList), [2, 1]) 


if __name__ == '__main__':
    unittest.main()
