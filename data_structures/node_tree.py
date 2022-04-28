"""This mod contains class Node for class BinarySearchTree"""


class NodeTree:
    """Node for Binary Tree"""

    def __init__(self, value):
        self._left = None
        self._value = value
        self._right = None

    @property
    def left(self):
        """Get left child"""
        return self._left

    @property
    def right(self):
        """Get right child"""
        return self._right

    @property
    def value(self):
        """Get value"""
        return self._value

    @left.setter
    def left(self, element):
        """Set value to left child"""
        self._left = element

    @right.setter
    def right(self, element):
        """Set value to right child"""
        self._right = element

    @value.setter
    def value(self, element):
        """Set new value"""
        self._value = element

    def __str__(self):
        return f'[Value={self.value}, Left={self.left}, Right={self.right}]'
