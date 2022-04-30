"""Testing class LinkedList"""

from data_structures.linked_list import LinkedList


def test_pend(more_numbers):
    """Check values in funcs prepend and append"""
    test_linked_list = LinkedList(5)
    test_linked_list.prepend(more_numbers)
    assert test_linked_list.head.value == more_numbers
    test_linked_list.append(more_numbers)
    assert test_linked_list.tail.value == more_numbers


def test_lookup(more_numbers):
    """Check look values by index"""
    test_linked_list = LinkedList(5)
    test_linked_list.append(more_numbers)
    for i in range(1, test_linked_list.count):
        assert test_linked_list.lookup(more_numbers) == i


def test_insert_wrong():
    """Check if we insert to wrong id"""
    test_linked_list = LinkedList(5)
    try:
        test_linked_list.insert(10, -2)
    except IndexError:
        assert True
    finally:
        assert test_linked_list.count == 1


def test_insert():
    """Check standard insert"""
    # create normal list
    test_list = LinkedList(5)
    test_list.prepend(3)
    # insert some value
    list_insert = LinkedList(5)
    list_insert.insert(3, 0)
    # check two lists
    assert str(test_list.head) == str(list_insert.head)


def test_delete_first_element():
    """Test about deleting first element from list"""
    test_list = LinkedList(5)
    test_list._delete_first_element()
    assert test_list.head is None and test_list.count == 0


def test_delete_some_node(more_numbers):
    """Test about delete some node by index"""
    check = LinkedList(5)
    # check to deleting by index
    test_list = LinkedList(5)
    test_list.append(more_numbers)
    for i in range(1, test_list.count):
        test_list._delete_some_node(i)
        assert str(check.head) == str(test_list.head)


def test_delete():
    """Test main func about delete"""
    # check to incorrect index
    check_list = LinkedList(5)
    try:
        check_list.delete(-99)
    except IndexError:
        assert True
    finally:
        assert check_list.count == 1
    # delete first index and first element
    new_list = LinkedList(3)
    new_list.delete(0)
    assert (new_list.head and new_list.tail) is None
    # check normal deleting
    check_list.append(3)
    check_list.delete(1)
    assert check_list.count == 1 and str(check_list.head) == str(LinkedList(5).head)
