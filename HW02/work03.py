"""
Требуется вывести все целые степени двойки (т.е. числа вида 2**k), не превосходящие числа N.
"""

n = int(input('Введите верхний лимит: '))
s = 1
print(f'{n} ->',end='')
while s < n:
    print(f' {s}',end='')
    s *= 2