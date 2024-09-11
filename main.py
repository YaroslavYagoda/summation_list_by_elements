"""
Напишите программу, которая создает два списка чисел и на их основе создаёт новый список.
В новом списке каждый элемент является суммой соответствующих элементов входных списков.
Программа должна делать это на основе циклов и работать со списками любой длины.
"""
from random import randint
from itertools import zip_longest

sp2 = [_ for _ in range(randint(0, 5_000))]
sp1 = [_ for _ in range(randint(0, 5_000))]

sp3 = [sum(i) for i in zip_longest(sp1, sp2, fillvalue=0)]
print(sp3)
