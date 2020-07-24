import string
import csv

def openfile(eenfile):
    file = open(eenfile, 'r')
    leeslines = file.readlines()
    file.close()
    return leeslines

t = openfile('apotheek_artikelen.csv')
for k in range(0,len(t)):
    lijnen = t[k]
    splitlijnen = lijnen.split(';')
    print(splitlijnen)

 