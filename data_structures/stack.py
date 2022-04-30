"""This mod contains class Stack"""

from data_structures.linked_list import LinkedList


class Stack(LinkedList):
    """This class implements work like a stack"""

    def push(self, element):
        """Add element to stack"""
        self.append(element)

    def pop(self):
        """Get last element from stack"""
        element = self.tail.value
        self.delete(self.count-1)
        return element

    def peek(self):
        """Just get value last element without pop"""
        return self.tail.value
