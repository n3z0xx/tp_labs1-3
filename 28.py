# 28. Создать 20 элементный список рандомных целых (-10, +10). Если в
# нем есть два соседних элемента одного знака, выведите эту пару. Если
# соседних элементов одного знака нет - не выводите ничего. Если таких
# пар соседей несколько - выведите первую пару
import random
egg = random.sample(range(-10,11), 20)
#print(egg)
for i in range(1, 21):
    if egg[i-1] >= 0 and egg[i] >= 0 or egg[i-1] < 0 and egg[i] < 0:
        print(egg[i-1], egg[i])
        break