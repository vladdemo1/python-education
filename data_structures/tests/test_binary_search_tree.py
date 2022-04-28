"""Testing class BinarySearchTree"""

import copy

from data_structures.binary_search_tree import BinarySearchTree
from data_structures.node_tree import NodeTree


def test_check_branch_to_value():
    """Test func about append to tree (we can or no)"""
    test_branch = BinarySearchTree(5)
    assert test_branch._check_branch_to_value(test_branch.head, True) is True
    assert test_branch._check_branch_to_value(test_branch.head, False) is True
    # then add two different element to left and right branches
    test_branch.insert(3)
    test_branch.insert(10)
    # check func when test branch have two branches
    assert test_branch._check_branch_to_value(test_branch.head, True) is False
    assert test_branch._check_branch_to_value(test_branch.head, False) is False


def test_select_branch():
    """Test func about get next move on branches (True if move to right)"""
    test_branch = BinarySearchTree(10)
    assert test_branch._select_branch(test_branch.head, 15) is True
    assert test_branch._select_branch(test_branch.head, 5) is False


def test_insert_to_empty_tree():
    """Test func if we insert value to empty tree"""
    test_tree = BinarySearchTree(5)
    test_tree.delete(5)
    # insert next value
    node_to_insert = BinarySearchTree(10)
    test_tree._insert_to_empty_tree(node_to_insert)
    assert test_tree.count == 1 and test_tree.head == node_to_insert


def test_insert_if_node_none():
    """Test helper func about insert if node none"""
    default_tree = BinarySearchTree(10)
    default_tree.delete(10)
    element = 10
    previous_node = NodeTree(5)
    node_to_insert = NodeTree(3)
    default_tree._insert_if_node_none(previous_node, node_to_insert, element)
    assert previous_node.right == node_to_insert


def test_insert_to_tree():
    """Test func about insert value to middle position in tree"""
    tree = BinarySearchTree(10)
    node = NodeTree(15)
    node_to_insert = NodeTree(20)
    tree._insert_to_tree(True, True, node, node_to_insert)
    assert node.right == node_to_insert and tree.count == 2


def test_insert():
    """Test main func about insert value to tree"""
    tree = BinarySearchTree(10)
    tree.insert(5)
    assert str(tree.head.left) == str(NodeTree(5))
    tree.insert(99)
    assert str(tree.head.right) == str(NodeTree(99))


def test_lookup():
    """Test func about get element(branch) by value"""
    tree = BinarySearchTree(10)
    tree.insert(15)
    tree.insert(25)
    # create deepcopy for check and check delete func too
    tree_check = copy.deepcopy(tree)
    tree_check.delete(10)
    assert str(tree.lookup(15).right) == str(NodeTree(25))


def test_check_and_delete_head():
    """Test func about deleting once element - head"""
    tree_one_element = BinarySearchTree(55)
    assert tree_one_element._check_and_delete_head(45) is False
    assert tree_one_element._check_and_delete_head(55) is True
    assert tree_one_element.count == 0


def test_check_empty_tree():
    """Test func about empty tree"""
    tree_to_delete = BinarySearchTree(4)
    assert tree_to_delete._check_empty_tree() is False
    tree_to_delete.delete(4)
    assert tree_to_delete._check_empty_tree() is True


def test_helper_to_delete_branch():
    """Test helper func about deleting value in tree"""
    tree = BinarySearchTree(1000)
    tree._position_branch = True
    tree._previous_branch = BinarySearchTree(30)
    tree._previous_branch.right = tree
    tree._helper_to_delete_branch(17)
    assert tree._previous_branch.right == 17


def test_delete_branch_without_children():
    """Test func about deleting branch if he hasn't children"""
    tree = BinarySearchTree(46)
    tree.insert(70)
    tree._delete_branch_without_children(tree.head.right)
    assert tree.count == 1 and tree.head.right is None


def test_delete_branch_with_left_children():
    """Test func about delete branch in situation when element have left children"""
    tree = BinarySearchTree(30)
    tree.insert(70)
    tree.insert(45)
    branch_to_delete = NodeTree(70)
    branch_to_delete.left = NodeTree(45)
    tree._del_branch_with_left_child(branch_to_delete)  # del 70
    assert str(tree.head.right) == str(branch_to_delete)


def test_delete_branch_with_right_children():
    """Test func about delete branch in situation when element have right children"""
    tree = BinarySearchTree(30)
    tree.insert(70)
    tree.insert(900)
    branch_to_delete = NodeTree(70)
    branch_to_delete.right = NodeTree(900)
    tree._del_branch_with_left_child(branch_to_delete)  # del 70
    assert str(tree.head.right) == str(branch_to_delete)


def test_delete_branch_with_two_children():
    """Test func if deleting element have two children"""
    tree = BinarySearchTree(5)
    tree.insert(100)
    tree.insert(10)
    tree.insert(150)
    # for check
    right_branch = NodeTree(10)
    right_branch.right = NodeTree(150)
    tree._del_branch_with_two_child(tree.head.right)
    assert str(tree.head.left) == str(right_branch)


def test_delete():
    """Test main func about delete selected element"""
    tree = BinarySearchTree(100)
    tree.insert(5)
    tree.insert(999)
    tree.insert(450)
    tree.delete(999)
    # for check
    test_branch = NodeTree(100)
    test_branch.left = NodeTree(5)
    test_branch.right = NodeTree(450)
    assert str(tree.head) == str(test_branch)
