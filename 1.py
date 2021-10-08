l = [i for i in range(-200, 201, 5) if int(i) % 2 == 0 and int(i) % 40 != 0]
print(l, "\n" + str(len(l)))