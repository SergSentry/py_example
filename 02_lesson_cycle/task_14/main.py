#
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

import math


if __name__ == '__main__':
    N = 1024
    tmp_digit = 1
    while tmp_digit < N:
        print(tmp_digit, end=' ')
        tmp_digit = tmp_digit << 1
