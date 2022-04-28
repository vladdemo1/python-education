"""This mode contains Node for Hash Table"""

from data_structures.node_base import NodeBase


class NodeTable(NodeBase):
    """This Node for Hash Table"""

    def __init__(self, value, hash_value, hash_link=None):
        super().__init__(value)
        self._hash_value = hash_value
        self._hash_link = hash_link

    @property
    def hash_value(self):
        """Get hash value"""
        return self._hash_value

    @hash_value.setter
    def hash_value(self, value):
        """Set new value to hash"""
        self._hash_value = value

    @property
    def hash_link(self):
        """Get hash value"""
        return self._hash_link

    @hash_link.setter
    def hash_link(self, value):
        """Set new value to hash"""
        self._hash_link = value

    def __str__(self):
        return f'[Value={self.value}, Hash={self.hash_value}, HashLink={self.hash_link}, Link={self.link}]'
