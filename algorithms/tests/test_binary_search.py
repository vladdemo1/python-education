"""This mod contains main tests about mod binary search"""


import pytest
from algorithms.binary_search import BinarySearch


@pytest.fixture
def get_mass():
    """Get simple mass"""
    return range(1000)


@pytest.mark.parametrize('value', [i for i in range(1000)])
def test_binary_search(get_mass, value):
    """Test about main func as binary search"""
    # check value in currently indexes
    binary = BinarySearch(get_mass, value)
    assert binary.index == value
    # this about first value and len mass (for searched index)
    if value == 0:
        value += 1
    # check index for reversed values
    next_binary = BinarySearch(get_mass, len(get_mass)-value)
    assert next_binary.index == len(get_mass) - value
