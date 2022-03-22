import unittest
from problems.reverse_linked_list import reverse_linked_list

# For testing
# obtain the list of values for the linked list


class LinkedListNode():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def linked_list_to_array(head):
    res = []
    while head:
        if head.val is not None:
            res.append(head.val)
            head = head.next
    return res

def array_to_linked_list(arr):
    if len(arr) == 0:
        return None
    else:
        head = LinkedListNode(arr[0])
        curr = head
        i = 1
        while i < len(arr):
            new_node = LinkedListNode(arr[i])
            curr.next = new_node
            curr = new_node
            i+=1
    return head


class TestReverseLinkedList(unittest.TestCase):
    def test1(self):
        nums = [1, 2, 3, 4, 5]
        head = array_to_linked_list(nums)
        new_head = reverse_linked_list(head)
        values = linked_list_to_array(new_head)
        nums.reverse()
        self.assertEqual(values, nums)

    def test2(self):
        nums = []
        head = array_to_linked_list(nums)
        new_head = reverse_linked_list(head)
        values = linked_list_to_array(new_head)
        nums.reverse()
        self.assertEqual(values, nums)

    def test3(self):
        nums = [1]
        head = array_to_linked_list(nums)
        new_head = reverse_linked_list(head)
        values = linked_list_to_array(new_head)
        nums.reverse()
        self.assertEqual(values, nums)

    def test4(self):
        my_list = array_to_linked_list([1, 2])
        reversed_list = reverse_linked_list(my_list)
        self.assertEqual(linked_list_to_array(reversed_list), [2, 1]) 

if __name__ == '__main__':
    unittest.main()
