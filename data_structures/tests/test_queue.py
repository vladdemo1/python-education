"""Testing class Queue"""

from data_structures.queue_new import Queue


def test_enqueue(more_numbers):
    """Test enqueue about add elements"""
    test_queue = Queue(5)
    test_queue.enqueue(more_numbers)
    assert test_queue.tail.value == more_numbers


def test_dequeue():
    """Test about deleting first elements"""
    # dequeue with one element
    test_queue = Queue(5)
    test_queue.dequeue()
    assert test_queue.head is None
    # dequeue with none elements in queue
    try:
        test_queue.dequeue()
    except IndexError:
        assert True
    finally:
        assert test_queue.count == 0
    # dequeue in normal situation
    next_queue = Queue(5)
    next_queue.enqueue(10)
    next_queue.dequeue()
    assert str(next_queue.head) == str(Queue(10).head)


def test_peek():
    """Testing about peek in Queue"""
    # check one element
    test_queue = Queue(1)
    assert test_queue.peek() == 1
    # add new elements and get peek
    test_queue.enqueue(2)
    test_queue.enqueue(3)
    assert test_queue.peek() == 1
    # delete all elements and check
    test_queue.dequeue()
    test_queue.dequeue()
    test_queue.dequeue()
    assert test_queue.peek() is None
