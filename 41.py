# 41. Сделать список из разной длины 12 подстрок, кот-ые формируются
# рандомно из вида альфанумерикал. Чтоб длины пуджстрок были от 1 до,
# например 10. Вывести индекс самой длинной подстроки и её саму!
import random
import string

MIN = 1
MAX = 10


def get_alphanumeric(length):
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length))


l = [get_alphanumeric(random.randint(MIN, MAX)) for _ in range(12)]
lmax = MIN - 1
imax = 0
for i in l:
    if len(i) > lmax:
        lmax = len(i)
        imax = l.index(i)

print(l[imax], len(l[imax]))