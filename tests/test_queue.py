import pytest
from geekshub_pyproblems.my_queue import Queue, QueueUnderflow, QueueOverflow, DEFAULT_QUEUE_SIZE


def test_create_queue_default_size():
    """ Tests to verify queues are created for various
        arguments
    """

    # Creating queue object without passing arguments
    q = Queue()
    assert isinstance(q, Queue) and q.max_slots == DEFAULT_QUEUE_SIZE and len(q) == 0

    # Creating queue object passing invalid object - string
    q = Queue('string')
    assert isinstance(q, Queue) and q.max_slots == DEFAULT_QUEUE_SIZE and len(q) == 0

    # Creating queue object passing invalid object - float
    q = Queue(10.0)
    assert isinstance(q, Queue) and q.max_slots == DEFAULT_QUEUE_SIZE and len(q) == 0

    # Creating queue object passing invalid object - None
    q = Queue(None)
    assert isinstance(q, Queue) and q.max_slots == DEFAULT_QUEUE_SIZE and len(q) == 0

    # Creating queue object with customer size = 20
    q = Queue(20)
    assert isinstance(q, Queue) and q.max_slots == 20 and len(q) == 0


def test_add_elements():
    """
    Tests to verify insertion of objects to the queue
    :return:
    """
    q = Queue(20)
    assert isinstance(q, Queue) and q.max_slots == 20 and len(q) == 0

    # Let us insert 20 elements and verify all get inserted properly
    for element in range(1, 21):
        q.add(element)
        assert len(q) == element

    # Let us try to add another element and this should fail now
    with pytest.raises(QueueOverflow):
        q.add(element + 1)


def test_retrieve_elements():
    queue_size = 10
    q = Queue(queue_size)
    for element in range(1, queue_size + 1):
        q.add(element)

    for index in range(1, queue_size + 1):
        assert q.retrieve() == index and len(q) == queue_size - index

    with pytest.raises(QueueUnderflow):
        q.retrieve()


def test_add_retrieve_heterogeneous_elements():
    queue_size = 5
    q = Queue(queue_size)
    assert isinstance(q, Queue) and q.max_slots == 5 and len(q) == 0

    q.add(None)
    q.add("Test")
    q.add([1, 2, 3, 4])
    q.add({1, 2, 3, 4, 5})
    q.add(True)
    assert len(q) == queue_size

    assert q.retrieve() == None and len(q) == queue_size - 1
    assert q.retrieve() == "Test" and len(q) == queue_size - 2
    assert q.retrieve() == [1, 2, 3, 4] and len(q) == queue_size - 3
    assert q.retrieve() == {1, 2, 3, 4, 5} and len(q) == queue_size - 4
    assert q.retrieve() == True and len(q) == queue_size - 5

    with pytest.raises(QueueUnderflow):
        q.retrieve()


def test_clear():
    q = Queue(20)
    assert isinstance(q, Queue) and q.max_slots == 20 and len(q) == 0

    # Let us insert 20 elements and verify all get inserted properly
    for element in range(1, 21):
        q.add(element)
        assert len(q) == element

    # let us clear
    q.clear()
    assert len(q) == 0

    with pytest.raises(QueueUnderflow):
        q.retrieve()


def test_membership_in():
    q = Queue()

    for item in range(6):
        q.add(item)

    for item in range(6):
        assert item in q


def test_membership_not_in():
    q = Queue()

    for item in range(6):
        q.add(item)

    for item in range(6, 20):
        assert item not in q