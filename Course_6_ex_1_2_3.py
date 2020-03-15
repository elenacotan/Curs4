import json
from collections import Counter

#Exercitiul 1

fisier = "text.txt"
fis = open(fisier)
ph = fis.read()
cuvinte = ph.split()
fis.close()

numarcuvinte=0

delimitatori = "., "
numaraparitii = {}
for linii in cuvinte:
    cuvant = linii.strip(delimitatori)
    numarcuvinte+=1
    if cuvant not in numaraparitii:
        numaraparitii[cuvant] = 0 
    numaraparitii[cuvant] += 1
print(numaraparitii)
print(numaraparitii.keys())
print(numaraparitii.values())
print(numaraparitii.items())
print(numarcuvinte)

#Exercitiul 2
frecventa = {k:(v/numarcuvinte)*100 for (k,v) in numaraparitii.items()}
print(frecventa)
print(frecventa.keys())
print(frecventa.values())
print(frecventa.items())


frecventa_removed = {k:v for (k,v) in frecventa.items() if v>5}
print(frecventa_removed)
print(frecventa_removed.keys())
print(frecventa_removed.values())
print(frecventa_removed.items())



with open('frecventa_removed.json', 'w') as f:
    json.dump(frecventa_removed, f)

#Exercitiul 3

with open('frecventa_removed.json', 'r') as f:
    frecventa3=json.load(f)
print(frecventa3)
print(frecventa3.keys())
print(frecventa3.values())
print(frecventa3.items())

#top 10 cuvinte cu cea mai mica frecventa
top_low = Counter(frecventa3).most_common(10)[-1]

for i in top_low:
    print(frecventa3)

