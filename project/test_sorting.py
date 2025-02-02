import pytest
from sorting import bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort

@pytest.fixture
def unsorted_data():
    return [8, 3, 1, 7, 1, 10, 2, 12, 4, 15, 5]

@pytest.fixture
def sorted_data():
    return [1, 1, 2, 3, 4, 5, 7, 8, 10, 12, 15]

def test_bubble_sort(unsorted_data, sorted_data):
    steps = []
    bubble_sort(unsorted_data, steps)
    assert unsorted_data == sorted_data

def test_selection_sort(unsorted_data, sorted_data):
    steps = []
    selection_sort(unsorted_data, steps)
    assert unsorted_data == sorted_data

def test_insertion_sort(unsorted_data, sorted_data):
    steps = []
    insertion_sort(unsorted_data, steps)
    assert unsorted_data == sorted_data

def test_merge_sort(unsorted_data, sorted_data):
    steps = []
    merge_sort(unsorted_data, steps)
    assert unsorted_data == sorted_data

def test_quick_sort(unsorted_data, sorted_data):
    steps = []
    quick_sort(unsorted_data, steps)
    assert unsorted_data == sorted_data