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
    for x in range(100):
        list1 = random.sample(range(100), 20)
        list2 = random.sample(range(100), 2)
        assert sorted(list1) == sorts.insertion_sort(list1)
        assert sorted(list2) == sorts.insertion_sort(list2)


def test_merge_sort():
    for x in range(100):
        list1 = random.sample(range(100), 20)
        list2 = random.sample(range(100), 2)
        assert sorted(list1) == sorts.merge_sort(list1)
        assert sorted(list2) == sorts.merge_sort(list2)


def test_merge_sorted_lists():
    for x in range(100):
        list1 = sorted(random.sample(range(100), 20))
        list2 = sorted(random.sample(range(100), 20))
        assert sorted(list1 + list2) == sorts.merge(list1, list2)
