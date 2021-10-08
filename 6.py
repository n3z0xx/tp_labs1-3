# 6. В бесконеч цикле вводить целое и выводить абс значения до пока не 0 и
# не через встр функцию.

while True:
    n = int(input())
    if n == 0: break
    if n < 0:
        print(n*-1)
    else:
        print(n)