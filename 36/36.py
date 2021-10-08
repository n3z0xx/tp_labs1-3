# 36. (файлов пока нет!!!! )Обратная: запись в файл рандомные числа —
# по одному в строку, диапазон -100 +100... Имя файла задавать через
# sys.argv.
import random
import sys

with open(sys.argv[1], 'w') as file:
    for _ in range(10):
        file.write(str(random.randint(-100, 100)) + "\n")