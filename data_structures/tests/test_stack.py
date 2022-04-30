"""Testing class Stack"""

import pytest
from data_structures.stack import Stack


@pytest.fixture
def more_numbers():
    """Get more numbers for append and prepend"""
    return range(1000000)


def test_push(more_numbers):
    """Testing about more push"""
    test_stack = Stack(5)
    test_stack.append(more_numbers)
    assert test_stack.tail.value == more_numbers


def test_pop():
    """Testing about pop"""
    value = 5
    test_stack = Stack(value)
    assert test_stack.pop() == value
    assert test_stack.head is None and test_stack.count == 0
    # check to another situation
    next_stack = Stack(3)
    next_stack.push(value)
    assert next_stack.pop() == value and str(next_stack.head) == str(Stack(3).head)


def test_peek(more_numbers):
    """Check stack about peek - just show last element value"""
    test_stack = Stack(5)
    test_stack.append(more_numbers)
    assert test_stack.peek() == more_numbers
