appendText='"'
names=open("capitalcities.txt",'r')
updatedname=open("name2.txt",'a')
for name in names:
    updatedname.write(appendText + name.rstrip() + appendText +"," '\n')

updatedname.close()
