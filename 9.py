# 9. зараз вывести все буквы лат алфавита, у кот код нечетный, потом по
# четному коду вывести соотв-щие буквы
print([chr(i) for i in range(ord("a"), ord("z")+1) if i % 2 != 0])
print([chr(i) for i in range(ord("a"), ord("z")+1) if i % 2 == 0])