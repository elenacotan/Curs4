'''Sa se scrie un program care citeste un string de la tastatura 
si afiseaza pe ecran fiecare cuvant din string pe cate o linie. 
Pentru a realiza acest lucru, se va folosi functia split. 
Separatorul dupa care se face despartirea este caracterul spatiu.'''

def words_split(my_str):
    words=my_str.split()
    for word in words:
      print(word)

my_str = input("Introduceti un string:")

words_split(my_str)