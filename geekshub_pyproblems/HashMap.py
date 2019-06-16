class HashMap:
    DEFAULT_MAP_SIZE = 20

    def __init__(self, size=DEFAULT_MAP_SIZE):
        if not isinstance(size, int) or size <= 0:
            self._size = HashMap.DEFAULT_MAP_SIZE
        else:
            # Maximum number of objects that can be stored
            self._size = size
        # Slots to store key-value pair
        self._map = [None] * self._size
        # Container to store the keys
        self._keys = []

    # Getters for attributes
    @property
    def size(self):
        return self._size

    @property
    def map(self):
        return self._map

    @property
    def keys(self):
        return self._keys

    # Special methods

    # method to return the length of HashMap
    def __len__(self):
        return len(self._keys)

    # method so that HashMap object can use indexing with keys
    def __getitem__(self, key):
        return self.get(key)

    # method so that HashMap object can use indexing with keys
    def __setitem__(self, key, value):
        return self.put(key, value)

    # Removes an entry from the HashMap using del operator
    def __delitem__(self, key):
        return self.delete(key)

    # Implement HashMap Iterator later
    def __iter__(self):
        return self.HashMapIterator(self._keys)

    # Get keys iterator
    def keys(self):
        return self.HashMapIterator(self._keys)

    # Get values iterator
    def values(self):
        return self.HashMapValueIterator(self)

    # Get key-value tuples as iterator
    def items(self):
        return self.HashMapItemIterator(self)

    # Our hashing is simple to reuse Python's hashing function
    def _hash(self, key):
        return hash(key)

    # Retrieve the value of given key from HashMap
    # raise KeyError if key not found
    def get(self, key):
        if key not in self._keys:
            raise KeyError('Key not found - ' + str(key))

        hashcode = self._hash(key)
        obj_list = self._map[hashcode % self.size]
        key_index = obj_list.index(key)
        return obj_list[key_index + 1]

    # Function that helps to add key-value to HashMap
    def put(self, key, value):
        hashcode = self._hash(key)

        # key is already present, we need to update the value
        if key in self._keys:
            obj_list = self._map[hashcode % self.size]
            key_index = obj_list.index(key)
            obj_list[key_index + 1] = value
        # if key is not present, we need to add
        else:
            obj_list = self._map[hashcode % self.size]
            if not obj_list:
                obj_list = []
                self._map[hashcode % self.size] = obj_list
                obj_list.append(key)
                obj_list.append(value)
            else:
                if key in obj_list:
                    key_index = obj_list.index(key)
                    obj_list[key_index + 1] = value
                else:
                    obj_list.append(key)
                    obj_list.append(value)

            # add to keys list as they key is not present
            self._keys.append(key)

    # Removes an entry from the HashMap
    def delete(self, key):
        if key not in self._keys:
            raise KeyError('Key not found' + str(key))

        hashcode = self._hash(key)
        obj_list = self._map[hashcode % self.size]

        # remove key and value from the container
        key_index = obj_list.index(key)
        object_in_list = obj_list[key_index + 1]
        obj_list.__delitem__(key_index)
        obj_index = obj_list.index(object_in_list)
        obj_list.__delitem__(obj_index)

        # remove the keys from global keys list
        key_index = self._keys.index(key)
        self._keys.__delitem__(key_index)

    def __str__(self):
        return str({str(key): str(value) for key, value in self.items()})

    # An iterator to iterate over keys
    class HashMapIterator:
        def __init__(self, keys):
            self._count = 0
            self._keys = keys

        def __iter__(self):
            return self

        def __next__(self):
            if self._count >= len(self._keys):
                raise StopIteration
            result = self._keys[self._count]
            self._count += 1
            return result

    # An iterator to iterate over value
    # Equivalent to dict.values()
    class HashMapValueIterator:
        def __init__(self, map):
            self._count = 0
            self._map = map

        def __iter__(self):
            return self

        def __next__(self):
            if self._count >= len(self._map):
                raise StopIteration
            result = self._map.get(self._map._keys[self._count])
            self._count += 1
            return result

    # An iterator to iterate over key, value as tuple
    # Equivalent to dict.items()
    class HashMapItemIterator:
        def __init__(self, map):
            self._count = 0
            self._map = map

        def __iter__(self):
            return self

        def __next__(self):
            if self._count >= len(self._map):
                raise StopIteration

            key = self._map._keys[self._count]
            result = key, self._map[key]
            self._count += 1
            return result
