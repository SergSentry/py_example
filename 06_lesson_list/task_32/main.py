#
# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума).
# Список можно задавать рандомно

import random


def new_random_list(a: int, b: int, n: int):
    return [random.randint(a, b) for i in range(n)]


def find_index(min: int, max: int, array:list[int]):
    return [i for i in range(len(array)) if min <= array[i] <= max]


if __name__ == '__main__':
    MIN = 25
    MAX = 75
    
    random_list = new_random_list(1, 100, 10)
    index = find_index(MIN, MAX, random_list)

    print("input", random_list)
    print("min", MIN)
    print("max", MAX)
    print("output", index)
