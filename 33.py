# 33. Заполните массив целыми числами начиная с нуля по строчкам, слева
# направо, строчки обходятся сверху вниз.
# 0 1 2 3 4 5
# 6 7 8 9 10 11
# 12 13 14 15 16 17
# 18 19 20 21 22 23
# 24 25 26 27 28 29
import pprint
a = [[int(i) for i in range(j*6-6,j*6)] for j in range(1, 6)]
pprint.pprint(a)