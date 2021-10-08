# 17. Через random.sample() (см. help) задать множество рандомных целых
# (10, 20) и вывеси его сумму, запомнив. Потом убирать любое одно и добавлять также любое и остановиться когда суммы совпали и сказать за
# сколько раз.
import random

foo = random.sample(range(10, 20), 10)
s = sum(foo)
print(s)
n = 0
while True:
    random.shuffle(foo)
    foo.pop()
    foo.append(random.randint(10, 20))
    if s == sum(foo): break
    n += 1
print(n)