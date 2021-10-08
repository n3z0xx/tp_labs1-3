# 15. создать множество из 10 рандомн целых (1,20) 
# и в цикле делать такое же второе до тех пор пока их пересечение 
# не будет пустым и считать за сколько попыток и вывести за сколько.
import random

a = set(random.sample(range(1, 20), 10))
b = set(random.sample(range(1, 20), 10))
n = 1
while True:
    b = set(random.sample(range(1, 20), 10))
    n += 1
    if a.intersection(b) == (): break
print(n)