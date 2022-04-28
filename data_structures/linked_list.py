"""This mod contains class Linked List"""

from data_structures.node_table import NodeBase


class LinkedList:
    """This class implements work like a linked list"""

    count = 0

    def __init__(self, value):
        node = NodeBase(value)
        self.head = node
        self.tail = node
        self.count += 1

        self._previous = None

    def prepend(self, element):
        """Add element to start position in list"""
        node = NodeBase(element, self.head)
        self.head = node
        self.count += 1

    def append(self, element):
        """Add element to finish position in list"""
        node = NodeBase(element)
        self.tail.link = node
        self.tail = node
        self.count += 1

    def lookup(self, element):
        """Search index by first in position selected element"""
        node = self.head
        index = 0
        while index != self.count:
            if node.value == element:
                return index
            index += 1
            node = node.link

    def insert(self, element, index):
        """Insert element to concrete position and move rest elements right"""
        element_node = NodeBase(element)
        if index < 0 or self.count < index:
            raise IndexError
        if index == 0:
            self.prepend(element)
        elif index == self.count:
            self.append(element)
        else:
            node = self.head
            counter = 0
            while counter != self.count:
                if counter == index - 1:
                    current_node_link = node.link
                    node.link = element_node
                    element_node.link = current_node_link
                    break
                counter += 1
                node = node.link

    def _delete_first_element(self):
        """If first element to delete"""
        if self.count != 0:
            self.head = self.head.link
            self.count -= 1

    def _delete_some_node(self, index: int):
        """If index in middle or and"""
        node = self.head
        counter = 0
        while counter != self.count:
            if counter == index:
                if node.link is None:
                    self._previous.link = None
                    self.count -= 1
                    break
                self._previous.link = node.link
                self.count -= 1
                break
            counter += 1
            self._previous = node
            node = node.link

    def delete(self, index):
        """Delete element by index"""
        if index > self.count or index < 0:
            raise IndexError
        if index == 0:
            self._delete_first_element()
        else:
            self._delete_some_node(index)
