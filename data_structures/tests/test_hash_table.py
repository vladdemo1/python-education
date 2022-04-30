"""Testing class HashTable"""
import copy

import pytest
from data_structures.hash_table import HashTable


def test_get_hash():
    """Test about get real hash value"""
    test_table = HashTable('demo')
    assert test_table._get_hash('vlad') == 3
    assert test_table.head.hash_value == 1


def test_insert():
    """Testing about insert value to hash table"""
    test_table = HashTable('vlad')
    test_table.insert('vlad')
    assert test_table.head.hash_value is not None
    # check collision
    assert str(test_table.head.hash_link) == str(HashTable('vlad').head)


def test_delete_other():
    """Test about deleting element in big table and check collision"""
    test_table = HashTable('vlad')
    test_table.insert('demo')
    test_table.delete(1)  # 1 - hash value a 'demo'
    assert test_table.count == 1 and test_table.head.link is None


def test_delete_first():
    """Test about delete first element in hash table"""
    test_table = HashTable('vlad')
    test_table._delete_first()
    assert test_table.count == 0 and test_table.head is None


def test_delete():
    """Test main func about delete element from table by hash"""
    test_table = HashTable('vlad')  # hash - 3
    test_table.insert('demo')  # hash - 1
    # check to delete first element when in table two element
    test_table.delete(3)
    assert test_table.head.value == 'demo' and test_table.count == 1
    # delete last and once element
    test_table.delete(1)
    assert test_table.count == 0 and test_table.head is None


def test_check_collision():
    """Test func about check collision"""
    test_table = HashTable('vlad')
    assert test_table._check_collision(test_table.head) is False
    test_table.insert('vlad')  # added element with collision
    assert test_table._check_collision(test_table.head) is True


@pytest.mark.parametrize('nodes', [(HashTable('vlad').head, HashTable('demo').head)])
def test_check_tail(nodes):
    """Test about helper func about deleting last element"""
    test_table = HashTable('vlad')
    # run this func
    test_table._check_to_next_tail(*nodes)
    # check result
    assert test_table.tail.hash_value == nodes[0].hash_value


def test_lookup():
    """Test func about lookup value by hash"""
    test_table = HashTable('oleksii')  # hash 2
    test_table.insert('vlad')  # hash 3
    test_table.insert('vlad')
    # for check
    check = copy.deepcopy(test_table)
    # lookup first
    assert test_table.lookup(2) == check.head.value
    # look end
    assert test_table.lookup(3) == check.head.link.value
