# 43. Создать дикт с запросом по сисаргв для числа элементов словаря. В
# качестве ключей выступали бы одноэлементные числовые кортежи, а в качестве значений пусть на первом шаге стоят None. 
# Потом вместо None поставить выбранный чойсем элемент из английского алфавита и вывести
# таким образом получившийся словарь.
import sys
import random

dic = {(i): None for i in range(int(sys.argv[1]))}
a = [chr(i) for i in range(ord("a"), ord("z") + 1)]
for i in range(int(sys.argv[1])):
    dic[i] = random.choice(a)
print(dic)