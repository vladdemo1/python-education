"""This mod contains main tests about mod recursive factorial"""


import math
import pytest
from algorithms.recursive_factorial import Factorial


@pytest.fixture
def zero_factorial():
    return Factorial(0)


def test_preliminary_check(zero_factorial):
    """Test func about get result in some situation"""
    assert zero_factorial._preliminary_check() == 1
    zero_factorial._value = -55
    assert zero_factorial._preliminary_check() is None
    zero_factorial._value = 4
    assert zero_factorial._preliminary_check() == 24


@pytest.mark.parametrize('value', [i for i in range(1, 1000)])
def test_recursive_factorial(value):
    """Test main func as recursive factorial"""
    factorial = Factorial(value)
    assert factorial.result == math.factorial(value)
