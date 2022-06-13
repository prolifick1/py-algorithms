from problems.mergesort import mergesort

def test_mergesort():
    def it_sorts_50431_to_01345():
        assert(mergesort([5, 0, 4, 3, 1]) == [0, 1, 3, 4, 5])
    def it_sorts_empty_to_empty():
        assert(mergesort([]) == []) 
    def it_sorts_55_to_55():
        assert(mergesort([55]) == [55])
    def it_sorts_12345_to_12345():
        assert(mergesort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5])
    def it_sorts_98765_to_56789():
        assert(mergesort([9, 8, 7, 6, 5]) == [5, 6, 7, 8, 9])
    def it_sorts_109_23_547_2_1_300_to_1_2_23_109_300_457():
        assert(mergesort([109, 23, 547, 2, 1, 300]) == [1, 2, 23, 109, 300, 457])
    def it_sorts_long_array_with_negatives():
        assert(mergesort([892, 23, 562, 46, 3, 1112, 9, 8, 99, -12, -30]) == [-30, -12, 0, 3, 9, 23, 46, 99, 562, 892, 1112])
