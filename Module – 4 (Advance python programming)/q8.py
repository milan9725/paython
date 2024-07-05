file=open("abc.txt")
p=file.read()
p=p.split()
m=p[0]
for i in p:
    if len(i)>len(m):
        m=i
print(m)
file.close()