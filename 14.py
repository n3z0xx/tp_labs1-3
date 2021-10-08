# 14. создать рандомн список из 20 целых (1,12) и срезами скопировать
# его в другой с конца через один
import random
a = [random.randint(1, 12) for _ in range(20)]
b = a[::-2]
int(a)
print(b)