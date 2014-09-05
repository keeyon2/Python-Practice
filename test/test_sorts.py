import sys
import os
import random
from practicemodules import sorts


def test_push_list_elements():
    assert sorts.push_list_elements(range(5), 0, 2) == [2, 0, 1, 3, 4]
    assert sorts.push_list_elements(range(10), 8, 9) == [0, 1, 2,
                                                         3, 4, 5,
                                                         6, 7, 9,
                                                         8]
    assert sorts.push_list_elements([1], 0, 0) == [1]
    assert sorts.push_list_elements(range(8), 3, 5) == [0, 1, 2, 5, 3, 4, 6, 7]


def test_insertion_sort():
    for x in range(10):
        list = random.sample(range(100), 20)
        list2 = random.sample(range(100), 2)
        assert sorted(list) == sorts.insertion_sort(list)
        assert sorted(list2) == sorts.insertion_sort(list2)
