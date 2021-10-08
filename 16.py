# 16. в цикле генерить рандомное целое (0, 12) и давать его в виде десятич, в виде бин, октал и хекс. Давать число в нем битов, останов по
# нулю
import random

while True:
    spam = random.randint(0, 12)
    print(spam, bin(spam), oct(spam), hex(spam), spam.bit_length())
    if spam == 0: break