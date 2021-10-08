# 7. Сделать произвольную строку из англ букв, отфильтровать гласные
# (aoeui) и перемешать ее 4 раза в цикле и вывести ориг и результат.
import random

l = "asdjkfensdfgjasdfhwuefioqwebfuief"
print(l)
l = [i for i in l if i not in ["a", "o", "e", "i", "u"]]
for _ in range(4):
    random.shuffle(l)
print("".join(l))