#На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
#Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были 
#повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

import random

from typing import List

a = ['emblem', 'tails']

coins = random.randint(1, 10)
coins_array: List[str] = []

for i in range(coins):
    coins_array.append(a[random.randint(0, 1)])

print(coins_array)

emblem_count = 0
tails_count = 0

for i in coins_array:
    if i == 'emblem':
        emblem_count += 1
    else:
        tails_count += 1

if (emblem_count == 1 and tails_count == 0) or (emblem_count == 0 and tails_count == 1):
    print(0)
elif emblem_count == tails_count:
    print(0)
elif emblem_count < tails_count:
    print(f'Переверните монетки с гербом  {emblem_count}')
else:
    print(f'Переверните монетки с решкой {tails_count}')
