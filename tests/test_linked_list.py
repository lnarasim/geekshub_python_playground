import pytest
from geekshub_pyproblems.linkedlist import Node, LinkedList


@pytest.fixture(scope='module')
def linked_list():
    lst = LinkedList()
    return lst


def test_linked_list_insert(linked_list):
    one = Node(1)
    two = Node()
    two.item = 2
    three = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)
    seven = Node(7)

    linked_list.insert(one)
    assert 1 in linked_list
    assert len(linked_list) == 1

    linked_list.insert(two)
    assert 2 in linked_list
    assert len(linked_list) == 2

    linked_list.insert(three)
    assert 3 in linked_list
    assert len(linked_list) == 3

    linked_list.insert(four)
    assert 4 in linked_list
    assert len(linked_list) == 4

    linked_list.insert(five)
    assert 5 in linked_list
    assert len(linked_list) == 5

    linked_list.insert(six)
    assert 6 in linked_list
    assert len(linked_list) == 6

    linked_list.insert(seven)
    assert 7 in linked_list
    assert len(linked_list) == 7

    # we have not inserted 10 to the list, let us find whether it is in the list
    assert 10 not in linked_list


def test_insert_linked_list_invalid(linked_list):

    with pytest.raises(TypeError):
        linked_list.insert(None)

    with pytest.raises(TypeError):
        linked_list.insert("sing")


def test_linked_list_clear(linked_list):
    node = Node(1)
    linked_list.insert(node)

    assert len(linked_list) > 0
    linked_list.clear()
    assert len(linked_list) == 0


def test_linked_list_delete(linked_list):
    linked_list.clear()
    assert len(linked_list) == 0

    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)
    seven = Node(7)

    linked_list.insert(one)
    linked_list.insert(two)
    linked_list.insert(three)
    linked_list.insert(four)
    linked_list.insert(five)
    linked_list.insert(six)
    linked_list.insert(seven)

    assert 1 in linked_list
    linked_list.delete(1)
    assert 1 not in linked_list

    assert 2 in linked_list
    linked_list.delete(2)
    assert 2 not in linked_list

    assert 5 in linked_list
    linked_list.delete(5)
    assert 5 not in linked_list

    assert 7 in linked_list
    linked_list.delete(7)
    assert 7 not in linked_list


def test_linked_list_reverse(linked_list):
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)
    seven = Node(7)

    linked_list.clear()

    linked_list.insert(one)
    linked_list.insert(two)
    linked_list.insert(three)
    linked_list.insert(four)
    linked_list.insert(five)
    linked_list.insert(six)
    linked_list.insert(seven)

    result = str(linked_list)
    assert result == '1-2-3-4-5-6-7'

    linked_list.reverse()
    result_rev = str(linked_list)
    assert result == result_rev[::-1]
