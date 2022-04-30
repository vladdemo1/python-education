"""This mod contains class about Binary Search"""


class BinarySearch:
    """This class can search index by value as binary"""

    def __init__(self, array, search_element):
        if array != sorted(array):
            self._array = sorted(array)
        else:
            self._array = array
        # create necessary properties
        self._search_element = search_element
        self._left = 0
        self._right = len(array) - 1
        self._result = self._binary_search()

    @property
    def index(self):
        """Get result (index) after binary search"""
        return self._result

    def _binary_search(self):
        """Main func about binary search"""
        while self._left <= self._right:
            middle = self._left + (self._right - self._left) // 2
            # if search element stay at middle
            if self._array[middle] == self._search_element:
                return middle
            # if search element greater current middle
            if self._array[middle] < self._search_element:
                self._left = middle + 1
                continue
            # if search element lower current middle
            self._right = middle - 1
        # after all operations - if we don't search element in array
        return None

    def __str__(self):
        if self.index is None:
            return f'Search value [{self._search_element}] was not found in the array!'
        return f'Search value = {self._search_element}, Index = {self.index}.'


if __name__ == '__main__':

    current_array = [23, 4, 90, 133, 583, 111, 2, 49, 70]
    search_value = 49
    # create and search
    binary = BinarySearch(current_array, search_value)
    # print result
    print(binary)
