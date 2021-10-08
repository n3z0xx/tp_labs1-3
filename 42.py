# 42. Создать множество сеткомпом из 10 букв русского, а фильтровать
# так, чтобы было 5 гласных 5 согласных, всяких, конечно.
import random

rus = [chr(i) for i in range(ord("а"), ord("е") + 1)] + ["ё"] + [chr(i) for i in range(ord("ж"), ord("я") + 1)]
a = ['а', 'е', 'ё', 'и', 'й', 'о', 'у', 'ы', 'э', 'ю', 'я']     # гласные
b = [i for i in rus if i not in a]                              # согласные

s1 = {i for i in random.sample(a, 5)}
s2 = {i for i in random.sample(b, 5)}
print(s1 | s2)