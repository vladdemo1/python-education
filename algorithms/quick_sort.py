"""This mod contains class about Quick Sort"""
import random


class QuickSort:
    """This class can sort array as quick"""

    def __init__(self, array):
        self._array = array
        self._container = [0] * (len(array) - 1)
        # get sorted array by quick sort
        self._quick_sort()

    @property
    def array(self):
        """Get sorted array"""
        return self._array

    def _quick_sort(self):
        len_array = len(self._array) - 1
        # create main index for this sorting
        index = 0
        # push default index to top at container
        self._container[index] = 0
        index += 1
        # push len as last index
        self._container[index] = len_array
        # while container is not empty
        while index >= 0:
            len_array = self._container[index]
            index -= 1
            # add value for low checker
            low = self._container[index]
            index -= 1
            # get index of pivot element
            pivot_index = self._get_index_pivot(low, len_array)
            # check about position element - maybe element it left
            if pivot_index - 1 > low:
                index += 1
                # push next low to container
                self._container[index] = low
                index += 1
                self._container[index] = pivot_index - 1
            # check about position element - maybe element it right
            if pivot_index + 1 < len_array:
                index += 1
                # push next index
                self._container[index] = pivot_index + 1
                index += 1
                # next
                self._container[index] = len_array

    def _get_index_pivot(self, low, high):
        # set current index
        index = low - 1
        pivot = self._array[high]
        for j in range(low, high):
            # check element to pivot
            if self._array[j] <= pivot:
                # increment index of smaller element
                index = index + 1
                self._array[index], self._array[j] = self._array[j], self._array[index]
        # change
        self._array[index + 1], self._array[high] = self._array[high], self._array[index + 1]
        # return index pivot
        return index + 1

    def __str__(self):
        return f'{self.array}'

    def __repr__(self):
        return self.array


if __name__ == '__main__':
    # create random array
    arr = [random.randint(1, 100) for _ in range(10)]
    print(f"Unsorted mass:\n{arr}")
    sort = QuickSort(arr)
    print("Sorted mass by quick sort:")
    print(sort)
