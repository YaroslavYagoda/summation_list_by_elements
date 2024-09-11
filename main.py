"""
Напишите программу, которая создает два списка чисел и на их основе создаёт новый список.
В новом списке каждый элемент является суммой соответствующих элементов входных списков.
Программа должна делать это на основе циклов и работать со списками любой длины.
"""
from random import randint as ri
from itertools import zip_longest as zl

# Решение с использованием знаний курса
sp2 = [i for i in range(3)]
sp1 = [i for i in range(2)]
sp3 = []

if len(sp1) > len(sp2):
    for i in range(len(sp2)):
        sp3.append(sp1[i] + sp2[i])
    for i in range(len(sp2), len(sp1)):
        sp3.append(sp1[i])
else:
    for i in range(len(sp1)):
        sp3.append(sp1[i] + sp2[i])
    for i in range(len(sp1), len(sp2)):
        sp3.append(sp2[i])

print(sp3)

# Решение в одну строку
print([sum(i) for i in zl([i for i in range(ri(0, 50))], [i for i in range(ri(0, 50))], fillvalue=0)])
