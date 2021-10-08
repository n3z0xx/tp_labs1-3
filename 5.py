# 5. ввести 2 числа — катета и вывести гипотенузу 2-мя способами и без
# sys.argv()
import sys
import math
a, b = map(int, input().split())
c = math.sqrt(a**2 + b**2)

# 1
print(c)

# 2
sys.stdout.write(str(c) + "\n")
sys.stdout.flush()