import string

def readfile(myfile):
    file = open(myfile, 'r')
    filelines = file.readlines()
    file.close()
    return filelines

art_dict = {}

x = readfile('apotheek_artikelen.csv')

for i in range(0,len(x)):
    regels = x[i]
    splitregels = regels.strip().lower().split(';')
    art_dict[splitregels[3]] = []
    
keylijst = art_dict.keys()
print(len(keylijst))