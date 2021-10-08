# 8. сделать список и 13 рандомн целых (1,20) и вывести сумму, ср арифм
# списка, а также ср арифм без крайних и медиану всего и без крайних.
import random
import statistics
l = [random.randint(1, 20) for _ in range(13)]
print("avg:", statistics.mean(l), statistics.mean(l[1:-1]))
print("median:", statistics.median(l), statistics.median(l[1:-1]))