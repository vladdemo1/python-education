"""This mod contains class HashTable"""

from data_structures.node_table import NodeTable


class HashTable:
    """This class implements work like a hash table"""

    count = 0
    hash_standard_len = 30

    def __init__(self, value):
        node = NodeTable(value, self._get_hash(value))
        self.head = node
        self.tail = node
        self.count += 1

    def _get_hash(self, value):
        """Create hash for current value"""
        summary = 0
        for char in value:
            summary += ord(char)
        return summary % self.hash_standard_len

    def insert(self, value):
        """Insert current value to current hash table"""
        hash_value = self._get_hash(value)
        node_to_insert = NodeTable(value, hash_value)
        index = 0
        node = self.head
        while index != self.count:
            if node is None:
                break
            if node.hash_value == hash_value:
                node.hash_link = node_to_insert
                self.count += 1
                return None
            index += 1
            node = node.link

        self.tail.link = node_to_insert
        self.tail = node_to_insert
        self.count += 1

    def _delete_other(self, hash_value):
        """Delete element by hash value and check maybe collision"""
        node = self.head
        node_previous = None
        counter = 0
        while counter != self.count:
            if node is None:
                break
            if node.hash_value == hash_value:
                if self._check_collision(node):
                    node.hash_link = None
                else:
                    node_to_delete = node_previous.link
                    self._check_to_next_tail(node_previous, node_to_delete)
                    node_previous.link = node_to_delete.link
                    break
            counter += 1
            node_previous = node
            node = node.link
        self.count -= 1

    def _delete_first(self):
        """If by hash value is a first_element"""
        if self.head.hash_link is None:
            self.head = self.head.link
        else:
            self.head.hash_link = None
        self.count -= 1

    def delete(self, hash_value):
        """Func about delete value by hash value"""
        if hash_value == self.head.hash_value:
            self._delete_first()
        else:
            self._delete_other(hash_value)

    @staticmethod
    def _check_collision(node: NodeTable):
        """Check collision if value insert to hash table"""
        if node.hash_link is not None:
            return True
        return False

    def _check_to_next_tail(self, node_now: NodeTable, node_next: NodeTable):
        """If element to delete is a tail"""
        if node_next is self.tail:
            self.tail = node_now

    def lookup(self, hash_value):
        """Get value by hash to look"""
        node = self.head
        index = 0
        while index != self.count:
            if node.hash_value == hash_value:
                return node.value
            index += 1
            node = node.link
        return None
