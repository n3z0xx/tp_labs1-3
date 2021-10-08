# 34. Даны 2 списка 5-и и 3-х элементный соответственно. Дайте три
# способа как вставить мЕньший в бОльший, пусть со 2-го места.
l1 = [1, 2, 3, 4, 5]
l2 = [0, 0, 0]

#* 1
def stupid(index):
    for i in range(index, len(l2)+index):
        l1.insert(i, l2.pop(0))
    print(l1)

#stupid(2)

#* 2
def use_slice_and_cc(index):
    print(l1[:index] + l2 + l1[index:])

#use_slice_and_cc(2)

#* 3
def just_slice(index):
    l1[index:index] = l2
    print(l1)

#just_slice(2)