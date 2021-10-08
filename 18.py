# 18. Через юникодные коды задать произвольную строку из 20 первых англ
# букв и вывести все индексы, где встречается буква «e»
import random
foo = "".join([chr(random.randint(ord("a"), ord("u"))) for _ in range(100)])
#print(foo)
for i in range(len(foo)):
    if foo[i] == "e": print(i)