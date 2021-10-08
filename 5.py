# 5. ввести 2 числа — катета и вывести гипотенузу 2-мя способами и без
# sys.argv()
import sys
import math
a, b = map(int, input().split())

# 1
print(math.sqrt(a**2 + b**2))

# 2
print(math.hypot(a, b))
