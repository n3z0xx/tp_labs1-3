# 29. В списке, состоящем из подстрок разной длины, найти самую минимальную по длине подстроку и дать индекс ее начала
import string
import random

MIN = 4
MAX = 12

def get_alphanumeric(length):
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length))


l = [get_alphanumeric(random.randint(MIN, MAX)) for _ in range(12)]
foo = [len(i) for i in l]
#print(l)
print(foo.index(min(foo)))