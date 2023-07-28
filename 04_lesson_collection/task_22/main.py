#
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа.
# n — кол-во элементов первого множества.
# m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

import random

if __name__ == '__main__':
    n = int(input("input n="))
    m = int(input("input m="))

    n_set = set()
    for ni in range(n):
        n_set.add(int(input(f"input n{ni}= ")))

    m_set = set()
    for mi in range(m):
        m_set.add(int(input(f"input m{mi}= ")))

    result = list(n_set.union(m_set))
    print("output", result)
