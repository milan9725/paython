n = int(input("Enter Lines To Read : "))
p = open("file.txt","r")
for i in range(n):
	print(p.readline())