"""Testing functions with math path"""

import pytest
from unittesting.to_test import even_odd, sum_all


@pytest.mark.parametrize('number', [14, 0, -56])
def test_even(number):
    """Test normal values for even"""
    assert even_odd(number)


@pytest.mark.parametrize('number', [21, -111, -11.3])
def test_odd(number):
    """Test normal values for odd"""
    assert even_odd(number)


def test_even_like_odd():
    """Test no correct value like even"""
    assert even_odd(28) == 'odd'


def test_odd_like_even():
    """Test no correct value like even"""
    assert even_odd(15) == 'even'


def test_by_zero():
    """Test about zero like odd"""
    assert even_odd(0) == 'odd'


@pytest.fixture()
def normal_num_list():
    """Get current time"""
    return range(5)


def test_sum_normal(normal_number_list):
    """Normal test for sum list numbers"""
    assert sum_all(*normal_number_list) == 10


def test_sum_various_types():
    """Test by various types numbers"""
    nums = [1, 0, -33.7, 3.7, 1000.0, 54]
    assert sum_all(*nums) == 1025.0


def test_sum_different_types():
    """Test for different types results"""
    nums = [1, 2.0, 7, -8.5, 0.5]
    assert sum_all(nums) == 2
