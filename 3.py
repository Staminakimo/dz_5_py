# Задача 3. Задайте список случайных чисел от 1 до 10.
# Посчитайте, сколько всего совпадающих элементов есть в списке. Удалите все повторяющиеся элементы.
# [1, 4, 2, 3, 4, 6, 1, 7] = > 4 элемента совпадают. Список уникальных элементов
# [1, 4, 2, 3, 6, 7]

import random
len_random_list = 10
random_list = list(random.randint(1, 10) for _ in range(10))
print(f'Наш список {random_list}')
result = list(map(lambda num: random_list.count(num) > 1, random_list))
print(f'Количество повторений в списке {result.count(True)}')
