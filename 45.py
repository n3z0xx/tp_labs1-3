# 45. Создать список греческого алфавита и вывести его с его буквами с
# начала и с конца, и количество его букв (от альфы до омеги пусть
# только заглавных).
a = [chr(i) for i in range(913,938) if i != 930]
print(a)
print(a[::-1])
print(len(a))
