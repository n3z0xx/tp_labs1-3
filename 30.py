# 30. Дана длинная строка из всевозможных элементов. Сначала проверить,
# чтоб она была всякая (альфанумерик).Потом надо оставить в ней только
# буквенные символы, а остальные перезаписать нулевыми символами

foo = "jsafdAKf12Jkf13Kf5gL"

if foo.isalnum():
    foo = ''.join([i for i in foo if str(i).isalpha()])
    print(foo)
else:
    print("Not alnum")