# 26. Задать словарь из 3-х айтемов. Значение (не ключ) каждого айтема
# (item) есть список из 5 целочисленных элементов. Программа должна вывести тот айтем, у которого сумма элементов значения минимальна
bar = {1:[1,2,3,4,5], 2:[5,4,1,2,1], 3:[2,3,4,5,6]}
foo = [sum(i) for i in bar.values()]
print(str(foo.index(min(foo))+1)+":",bar[foo.index(min(foo))+1])
