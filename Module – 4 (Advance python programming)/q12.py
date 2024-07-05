with open('Tops.txt','r') as topsfile, open('abc.txt','a') as abcfile: 
    for line in topsfile:
       secondfile.write(line)