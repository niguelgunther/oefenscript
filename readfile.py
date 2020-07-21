import string

def readfile(myfile):
    file = open(myfile, 'r')
    filelines = file.readlines()
    file.close()
    return filelines

x = readfile('apotheek_artikelen.csv')
for i in range(0,len(x)):
    regels = x[i]
    splitregels = regels.split(';')
    print(splitregels)