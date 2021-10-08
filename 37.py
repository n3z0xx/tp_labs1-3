# 37. Из англ букв составить 13 элем-ую рандомную строку и убрать все
# неуникальные, заменив уникальные символом 0 (ноль). Вывести оставшиеся с их индексами.
import random
import string

s = ''.join(random.choice(string.ascii_lowercase) for _ in range(13))
print(s)
known = []
not_uniq = []
for i in s:
    if i not in known:
        known.append(i)
    else:
        not_uniq.append(i)

a = [i for i in s if i not in not_uniq]
#print(''.join(a))
print({s.index(i): i for i in a})