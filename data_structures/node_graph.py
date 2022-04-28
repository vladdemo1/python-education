"""This mod contains node for graph"""

from data_structures.node_base import NodeBase
from data_structures.linked_list import LinkedList


class NodeGraph(NodeBase):
    """Node for class Graph"""

    def __init__(self, value, connections: LinkedList = None):
        super().__init__(value)
        self._connections = connections

    @property
    def connections(self):
        """Get current nodes"""
        return self._connections

    @connections.setter
    def connections(self, next_connections):
        """Set next connections"""
        self._connections = next_connections

    def __str__(self):
        if self.connections is None:
            return f'[Value={self.value}, Connections={self.connections}, Link={self.link}]'
        return f'[Value={self.value}, Connections={self.connections.head}, Link={self.link}]'
