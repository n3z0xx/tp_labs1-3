# 23. через list comprehension вывести на экран в одну 
# строчку английский алфавит из прописных и строчных букв (с учетом последних z)

print([chr(i) for i in range(ord("A"), ord("Z")+1)] + [chr(i) for i in range(ord("a"), ord("z")+1)])