"""This mod contains main tests about mod quick sort"""
import random

import pytest
from algorithms.quick_sort import QuickSort


@pytest.fixture
def get_unsorted_mass():
    """Get big unsorted mass"""
    return [random.randint(1, 1000) for _ in range(1000)]


@pytest.mark.parametrize('value', (range(1000)))
def test_main_quick_sort(get_unsorted_mass, value):
    """Main test about work func QuickSort in 1000 iters about something situation"""
    assert QuickSort(get_unsorted_mass).array == sorted(get_unsorted_mass)
    # added parametrize for 1000 iterations this test and ...
    # create more different situations


def test_get_index_pivot():
    """Test func about get index pivot"""
    something_mass = [2, 45, 23, 11, 4, 19, 1]
    quick = QuickSort(something_mass)
    # this func not need to test, because ...
    # in this func contains refresh elements for main mass by self.
    assert quick._get_index_pivot(0, len(something_mass)-1) == len(something_mass)-1
