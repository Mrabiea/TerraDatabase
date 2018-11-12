appendText = '"'
names = open("capitalcities.txt", 'r')
updatedname = open("name2.txt", 'a')
for line in names:
    liste = line.split()
    word=":".join(liste)
    # if len(liste)>1:
    updatedname.write(appendText +word+ appendText + "," '\n')

updatedname.close()
