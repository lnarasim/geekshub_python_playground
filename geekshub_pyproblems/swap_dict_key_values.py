def swap_dict_keys_values(d):
    """Given a dictionary, this functions another dictionary with keys and values swapped"""
    if not isinstance(d, dict):
        raise TypeError

    new_dict = dict()
    for key, value in d.items():
        if value in new_dict:
            if isinstance(new_dict[value], list):
                new_dict[value].append(key)
            else:
                new_dict[value] = [new_dict[value], key]
        else:
            new_dict[value] = key

    return new_dict


dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 1, 'e': 1}
print(swap_dict_keys_values(dictionary))
