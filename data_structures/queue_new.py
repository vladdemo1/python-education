"""This mod contains class Queue"""

from data_structures.linked_list import LinkedList


class Queue(LinkedList):
    """This class implements work like a queue"""

    def enqueue(self, element):
        """Add element to finish in queue"""
        self.append(element)

    def dequeue(self):
        """Withdraw element from start position in queue"""
        self.delete(0)

    def peek(self):
        """Just get value element from start queue without withdraw"""
        if self.head is None:
            return None
        return self.head.value
