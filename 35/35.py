# 35. Дан текстовый файл, в каждой строчке по числу (интовое или флоат).
# Через sys.argv найти в указанном файле и вывести макс и мин число и номера их строк?
import sys

try:
    with open(sys.argv[1], 'r') as file:
        text = file.read()
        l = [float(i) for i in text.split()]
        print("max:", max(l), "line:", l.index(max(l))+1)
        print("min:", min(l), "line:", l.index(min(l))+1)
except FileNotFoundError:
    print("File doesn't exist")

