import csv

file = open('apotheek_artikelen.csv', 'r')

lezen = csv.reader(file)

art = {}

for row in lezen:
    art = {'Knmp':row[0],'Voorraad':row[1],'Location':row[3],'ArtikelNaam':row[4]}
    print(art)