"""This mod contains class Graph"""

from data_structures.node_graph import NodeGraph
from data_structures.linked_list import LinkedList


class Graph:
    """This class implements work like a graph"""

    count = 0

    def __init__(self, value):
        node = NodeGraph(value)
        self.head = node
        self.tail = node
        self.count += 1
        # property for deleting some element
        self._previous = None

    def insert(self, value: int, *args: int):
        """Add element with value and with links about others elements"""
        # if we have already this value
        if self.lookup(value) is not None:
            return None

        # just a insert
        node_to_insert = NodeGraph(value)
        self.tail.link = node_to_insert
        self.tail = node_to_insert
        self.count += 1

        # run from all connection
        len_args = len(args)
        index = 0
        node = self.head
        while index != self.count:
            # if node is None:
            #     break
            index_args = 0
            while index_args != len_args:
                if node.value == node_to_insert.value:
                    for char in args:
                        self._add_connections(node, char)
                    index_args += 1
                    break

                if node.value == args[index_args]:
                    # add connections
                    self._add_connections(node, node_to_insert.value)
                index_args += 1
            index += 1
            node = node.link

    @staticmethod
    def _add_connections(node: NodeGraph, value_to_insert):
        if node.connections is None:
            node.connections = LinkedList(value_to_insert)
        else:
            node.connections.append(value_to_insert)

    def lookup(self, value: int):
        """Search node by value and return link for this node"""
        node = self.head
        index = 0
        while index != self.count:
            if node.value == value:
                return node
            index += 1
            node = node.link
        return None

    def _delete_only_element(self, value):
        if self.count == 1 and self.head.value == value:
            self.head = None
            self.count -= 1
            return True
        return False

    def _delete_just_element(self, value):
        node = self.head
        index = 0
        while index != self.count:
            if node.value == value:
                if node.link is None:
                    self._previous.link = None
                    self.count -= 1
                    break
                self._previous.link = node.link
                self.count -= 1
                break
            index += 1
            self._previous = node
            node = node.link

    def _delete_all_connections(self, deleted_value):
        node = self.head
        index = 0
        while index != self.count:
            # delete connections by func delete in custom LinkedList
            # search deleting index
            index = node.connections.lookup(deleted_value)
            # deleting connect by index
            node.connections.delete(index)
            # next round
            index += 1
            node = node.link

    def delete(self, value: int):
        """Delete node by value and other nodes with this node"""
        # if graph have only element
        if self._delete_only_element(value):
            return None
        # if deleting element not in graph
        if self.lookup(value) is None:
            return None
        # firstly we need delete element and then - connections
        self._delete_just_element(value)
        # and then - deleting all connections
        self._delete_all_connections(value)
        return None
