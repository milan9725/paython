from collections import Counter
file=open("abc.txt")
p=file.read().split()
print(Counter(p))
file.close()