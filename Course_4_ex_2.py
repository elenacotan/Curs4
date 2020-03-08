''' Sa se scrie o functie care primeste ca parametri de intrare lungimea
 si latimea unui dreptunghi si returneaza aria acestuia. In cazul in care 
 latimea nu este data ca parametru la apel, sa se calculeze aria patratului 
 cu latura egala cu lungimea. Parametrul formal latime va trebui sa aiba o 
 valoare implicita setata in antetul functiei, de exemplu 0. Astfel, in 
 interiorul functiei, daca primim valoarea 0 pentru latime, stim ca avem 
 de a face cu un patrat.'''

def aria(lungime , latime=0):
    if latime==0:
        A=lungime*lungime
    else:
        A=lungime*latime
    return A

x = int(input("Introduceti valoarea intreaga aferenta lungimii x: "))
y = int(input("Introduceti valoarea intreaga aferenta latimii y: "))

print(aria(x,y))
print(aria(x))