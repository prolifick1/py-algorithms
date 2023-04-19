from problems.mergesort import merge_sort

#def test_mergesort():
#    def it_sorts_50431_to_01345():
#        assert(mergesort([5, 0, 4, 3, 1]) == [0, 1, 3, 4, 5])
#    def it_sorts_empty_to_empty():
#        assert(mergesort([]) == []) 
#    def it_sorts_55_to_55():
#        assert(mergesort([55]) == [55])
#    def it_sorts_12345_to_12345():
#        assert(mergesort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5])
#    def it_sorts_98765_to_56789():
#        assert(mergesort([9, 8, 7, 6, 5]) == [5, 6, 7, 8, 9])
#    def it_sorts_109_23_547_2_1_300_to_1_2_23_109_300_457():
#        assert(mergesort([109, 23, 547, 2, 1, 300]) == [1, 2, 23, 109, 300, 457])
#    def it_sorts_long_array_with_negatives():
#        assert(mergesort([892, 23, 562, 46, 3, 1112, 9, 8, 99, -12, -30]) == [-30, -12, 0, 3, 9, 23, 46, 99, 562, 892, 1112])
#

import unittest

class TestMergeSort(unittest.TestCase):
    def test_merge_sort(self):
        # Test case 1: Empty input array
        arr1 = []
        expected1 = []
        result1 = merge_sort(arr1)
        self.assertEqual(result1, expected1)
        
        # Test case 2: Array with a single element
        arr2 = [1]
        expected2 = [1]
        result2 = merge_sort(arr2)
        self.assertEqual(result2, expected2)
        
        # Test case 3: Array with duplicate elements
        arr3 = [5, 3, 8, 2, 5, 9, 1, 7, 5]
        expected3 = [1, 2, 3, 5, 5, 5, 7, 8, 9]
        result3 = merge_sort(arr3)
        self.assertEqual(result3, expected3)
        
        # Test case 4: Array with negative numbers
        arr4 = [-10, 5, -2, 0, -7, 3]
        expected4 = [-10, -7, -2, 0, 3, 5]
        result4 = merge_sort(arr4)
        self.assertEqual(result4, expected4)
        
        # Test case 5: Array with already sorted elements
        arr5 = [1, 2, 3, 4, 5, 6, 7]
        expected5 = [1, 2, 3, 4, 5, 6, 7]
        result5 = merge_sort(arr5)
        self.assertEqual(result5, expected5)
        
        # Test case 6: Array with reverse sorted elements
        arr6 = [7, 6, 5, 4, 3, 2, 1]
        expected6 = [1, 2, 3, 4, 5, 6, 7]
        result6 = merge_sort(arr6)
        self.assertEqual(result6, expected6)

if __name__ == '__main__':
    unittest.main()

