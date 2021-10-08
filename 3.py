# 3. Зараз (на раз) создать словарь с ключами, которые есть числа от 1 до
# 26 и значениями, которые есть буквы лат алфавита.
import string

print(dict((i, j) for i, j in enumerate(string.ascii_lowercase, start=1)))

