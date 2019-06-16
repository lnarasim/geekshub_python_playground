from collections import defaultdict


def word_frequency(sentence):
    if not isinstance(sentence, str):
        raise TypeError

    words = sentence.split(' ')
    word_dict = defaultdict(int)

    for word in words:
        word_dict[word] += 1

    return word_dict


def pyramid_gen(number, step=1):
    num_star = 1
    while True:
        yield ' ' * (number - num_star) + '*' * num_star
        num_star += step
        if num_star > number:
            break
    return


p_gen = pyramid_gen(8, 2)

for _ in range(4):
    print(next(p_gen))