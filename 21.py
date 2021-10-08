# 21. из строки «mama myla ramu» сделать 3-х элем-ный список и, потом,
# как то срезав у него «ama yla amu», слить остатки и в конце вывести
# уже оставшуюся опять строку, но не «mmr», а «Mmr»
egg = "mama myla ramu"
egg = egg.split()
foo = [i[:1] for i in egg]
bar = ''.join(foo)
print(bar.capitalize())