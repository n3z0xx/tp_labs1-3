# 11. задать список из 100 рандомных (0, 50) и вывести сколько чисел в
# каждом десятке
import random
foo = [random.randint(0, 50) for _ in range(100)]
c = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0}
for i in foo:
    c[(i//10)] += 1
print(c)