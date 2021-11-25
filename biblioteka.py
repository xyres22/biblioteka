import random
import time
date = time.strftime("%d/%m/%Y")

# Klasa przechowujaca filmy
class Film:
    def __init__(self,tytul,rok,gatunek,liczba_odtworzen):
        self.tytul = tytul
        self.rok = rok
        self.gatunek = gatunek
        self.liczba_odtworzen = liczba_odtworzen
    
    def __str__(self):
        return f'{self.tytul} ({self.rok})'

    # metoda dodajaca odtworzenie do danego tytulu
    def play(self):
        self.liczba_odtworzen += 1
      

film1 = Film('Eurotrip','2000','komedia', 1234)
film2 = Film('Titanic', '1980', 'dramat', 12)
film3 = Film('Harry Potter', '2005', 'fikcja', 250000)
film4 = Film('Hobbit', '2017', 'fikcja', 218000)


# klasa Seriali ktora dziedziczy atrybuty z Filmow
class Serial(Film):
    def __init__(self, odcinek, sezon, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.odcinek = odcinek
        self.sezon = sezon
        

    def __str__(self):
        return f'{self.tytul} S{self.sezon:02d}E{self.odcinek:02d}'

 
serial1 = Serial(65, 7, 'Dexter', '2005', 'dramat', 987654)
serial2 = Serial(12,8, 'Flash', '2015', 'fikcja', 500000)
serial3 = Serial(12, 4, 'Arrow', '2008', 'fikcja', 100000)
serial4 = Serial(2,4,'Gra o Tron', '2018', 'fikcja', 1000000)

# lista przechowujaca seriale i filmy !
list = [film1, film2, film3, film4, serial1, serial2, serial3, serial4]

print('Biblioteka filmów :')
g = 1
for i in list:
    print(f'{g}. {i}')
    g += 1

#metoda do wywolania filmow z listy
def get_movies(list):
    l = []
    for i in list:
        if type(i) is Film:
            l.append(i)

    l.sort(key=lambda film: film.tytul)

    for i in l:
        print(i)


# metoda do wywolania seriali z listy
def get_series(list):
    g = []
    for i in list:
        if type(i) is Serial:
            g.append(i)

    g.sort(key=lambda serial: serial.tytul)

    for i in g:
        print(i)

    
# Napisz funkcję search, która wyszukuje film lub serial po jego tytule.
def search(title):
    for i in list:
        if i.tytul.lower() == title.lower() :
            print(i)

print()
print()

# Napisz funkcję generate_views, która losowo wybiera element z biblioteki, a następnie dodaje mu losową (z zakresu od 1 do 100) ilość odtworzeń
def generate_views():
    view = random.choice(list)
    print(f'{view.tytul} posiada {view.liczba_odtworzen} wyswietleń przed akcja.')
    view.liczba_odtworzen += random.randint(1,100)
    print(f'{view.tytul} posiada {view.liczba_odtworzen} wyswietleń po akcja.')

generate_views()


# Napisz funkcję, która uruchomi generate_views 10 razy.
def multiple_views():
    for i in range (10):
        generate_views()

print()
print(f'Najpopularniejsze filmy i seriale dnia {date} to:')

# Napisz funkcję top_titles(), która zwróci wybraną ilość najpopularniejszych tytułów z biblioteki
def top_titles(ilosc, content_type):
    film = []
    serial = []
    for i in list:
        if type(i) is Film:
            film.append(i)
        else:
            serial.append(i)
    film.sort(key=lambda list: list.liczba_odtworzen, reverse=True)
    serial.sort(key=lambda list: list.liczba_odtworzen, reverse=True)
    if content_type == Film:
        for i in film[:ilosc]:
            print(f'{i.tytul} ma {i.liczba_odtworzen} wyswietlen!')
    if content_type == Serial:
        for i in serial[:ilosc]:
            print(f'{i.tytul} ma {i.liczba_odtworzen} wyswietlen!')

  
top_titles(3, Serial)