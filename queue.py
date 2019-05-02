DEFAULT_QUEUE_SIZE = 10


class Queue:

    def __init__(self, max_slots=DEFAULT_QUEUE_SIZE):
        if not isinstance(max_slots, int) or max_slots < 1:
            self.max_slots = DEFAULT_QUEUE_SIZE
        else:
            self.max_slots = max_slots
        self._container = []

    def add(self, an_object):
        if len(self._container) < self.max_slots:
            self._container.append(an_object)
        else:
            raise QueueOverflow("Queue is full")

    def retrieve(self):
        if len(self._container) > 0:
            return self._container.pop(0)
        else:
            raise QueueUnderflow("Queue is empty")

    def __len__(self):
        return len(self._container)


class QueueOverflow(Exception):
    def __init__(self, message):
        self.message = message


class QueueUnderflow(Exception):
    def __init__(self, message):
        self.message = message
