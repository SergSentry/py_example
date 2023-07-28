#
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
#    чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

import random

if __name__ == '__main__':
    N_COIN = 10
    attempt = []
    for i in range(0, N_COIN):
        attempt.append(random.randint(0,1))

    one_side = 0
    for i in range(0, N_COIN):
        if attempt[i]:
            one_side += 1
    
    if one_side > N_COIN/2:
        print(N_COIN - one_side)
    else:
        print(one_side)
