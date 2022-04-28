"""This mod contains class Node for basic structures"""


class NodeBase:
    """Node for base structures"""

    def __init__(self, value, link=None):
        self._value = value
        self._link = link

    @property
    def link(self):
        """Get link"""
        return self._link

    @property
    def value(self):
        """Get value"""
        return self._value

    @link.setter
    def link(self, element):
        """Set new link"""
        self._link = element

    @value.setter
    def value(self, element):
        """Set new value"""
        self._value = element

    def __str__(self):
        return f'[Value={self.value}, Link={self.link}]'
