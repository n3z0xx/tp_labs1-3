# 2. Построить и вывести список всех заглавных букв русского алфавита от А
# до Я. Через листкомп, слайсы и коды для русского из таблицы Юникода.

print([chr(i) for i in range(ord("А"), ord("Е")+1)] + ["Ё"] + [chr(i) for i in range(ord("Ж"), ord("Я")+1)])