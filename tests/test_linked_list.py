import pytest
from geekshub_pyproblems.linkedlist import Node, LinkedList

def test_linkedlist_insert():
    linked_list = LinkedList()
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


def test_insert_linkedlist_invalid():
    linked_list = LinkedList()

    with pytest.raises(TypeError):
        linked_list.insert(None)

    with pytest.raises(TypeError):
        linked_list.insert("sing")


def test_linkedlist_clear():
    lst = LinkedList()
    node = Node(1)

    lst.insert(node)
    assert len(lst) == 1
    lst.clear()
    assert len(lst) == 0


def test_linkedlist_delete():
    lst = LinkedList()
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)
    seven = Node(7)

    lst.insert(one)
    lst.insert(two)
    lst.insert(three)
    lst.insert(four)
    lst.insert(five)
    lst.insert(six)
    lst.insert(seven)

    assert 1 in lst
    lst.delete(1)
    assert 1 not in lst

    assert 2 in lst
    lst.delete(2)
    assert 2 not in lst

    assert 5 in lst
    lst.delete(5)
    assert 5 not in lst

    assert 7 in lst
    lst.delete(7)
    assert 7 not in lst

def test_linked_list_reverse():
    lst = LinkedList()
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)
    seven = Node(7)

    lst.insert(one)
    lst.insert(two)
    lst.insert(three)
    lst.insert(four)
    lst.insert(five)
    lst.insert(six)
    lst.insert(seven)

    result = lst.get_linked_lst_str()
    assert result == '1-2-3-4-5-6-7'

    lst.reverse()
    result = lst.get_linked_lst_str()
    assert result == '7-6-5-4-3-2-1'
