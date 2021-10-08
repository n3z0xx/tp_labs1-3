# 27. Создать 30 элементный список рандомных целых чисел (от -40 до
# +100). Вывести абс сумму отрицат-х и полож-х, потом среднее арифметическое и среднее геометрическое этих двух сумм
import random
from scipy.stats.mstats import gmean
from scipy import mean
egg = random.sample(range(-40,101), 20)
pos = [abs(i) for i in egg if i < 0]
neg = [abs(i) for i in egg if i >= 0]
print("sum pos:", sum(pos), "sum neg:", sum(neg))
print("arif mean of pos:", mean(pos), "gmean:", gmean(pos))
print("arif mean of neg:", mean(neg), "gmean:", gmean(neg))
