name = ['priyank','gaurav','moin','milan']
with open('abc.txt', "w") as myfile:
        for n in name:
                myfile.write("%s\n" % n)

file = open('abc.txt')
print(file.read())