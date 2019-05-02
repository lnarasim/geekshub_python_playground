# A simple stack implementation with push and pop of objects with stack containing fixed number of slots

DEFAULT_STACK_SIZE = 10


class Stack:

    def __init__(self, max_slots=DEFAULT_STACK_SIZE):
        if not isinstance(max_slots, int) or max_slots < 1:
            self.max_slots = DEFAULT_STACK_SIZE
        else:
            self.max_slots = max_slots
        self._container = []

    def push(self, an_object):
        if len(self._container) < self.max_slots:
            self._container.append(an_object)
        else:
            raise StackOverflow("Stack is full")

    def pop(self):
        if len(self._container) > 0:
            return self._container.pop(len(self._container) - 1)
        else:
            raise StackUnderflow("Stack is empty")

    def __len__(self):
        return len(self._container)


class StackOverflow(Exception):

    def __init__(self, message):
        self.message = message


class StackUnderflow(Exception):

    def __init__(self, message):
        self.message = message
