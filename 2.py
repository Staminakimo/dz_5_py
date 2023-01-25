# Задача 2. Дан список случайных чисел. Создайте список, в который попадают числа,
# описывающие случайную возрастающую последовательность. Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] = [1, 2, 3] или[2, 7] или[4, 6, 7] и т.д.

import random
length = 10
random_list = [random.randint(1, 10) for _ in range(length)]
print(f'Наш список {random_list}')
i = random.randint(0, len(random_list)-1)
result = [random_list[i]]
while i < len(random_list):
    i = random.randint(i, len(random_list))
    if i != len(random_list) and random_list[i] > result[-1]:
        result.append(random_list[i])
print(result)
