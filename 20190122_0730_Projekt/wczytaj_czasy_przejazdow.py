#Skrypt wyznaczenia macierzy czasu przejazdu między lokalizacjami (przejazd samochodem)
import json
import urllib.request

naglowek = 'https://maps.googleapis.com/maps/api/distancematrix/json?'

#klucz api
apiKey = 'AIzaSyACkaQxRFX-XCrLKEuWTMx9W0o5GBVwD_g'


poczatek = ""
koniec = ""
zadanie = ""
req = ""
resp = ""
result = " "
kierunek = ""

wynik = 0
odpowiedz = ""

#wielkość macierzy
count = 31

cnt = 1

tab = []

coordinates = []

for i in range(count):
    tab.append([])
    for j in range(count):
        tab[-1].append(" ")


#wczytanie pliku macierz.txt
fd = open("plik_danych_wsp.txt", "r")

for line in fd:
    wiersz = line.strip("\n")
    print(wiersz)
    coordinates.append(wiersz)

fd.close()

for x in range(1,count):
    tab[0][x] = coordinates[x-1]
    tab[x][0] = coordinates[x-1]




fd = open("czasy_przejazdow.csv", "w")


for y in range(1,count):

    for z in range(1, count):
        poczatek = tab[y][0]
        koniec = tab[0][z]
        zadanie = 'origins={}&destinations={}&key={}'.format(poczatek, koniec, apiKey)

        req = naglowek + zadanie
        resp = urllib.request.urlopen(req).read()

        kierunek = json.loads(resp)

        wynik = kierunek['rows'][0]['elements'][0]['duration']['value']
        odpowiedz = str(y-1)
        odpowiedz += ";"
        odpowiedz += str(z-1)
        odpowiedz += ";"
        odpowiedz += str(wynik)
        odpowiedz += ";"

        fd.write(odpowiedz)

        fd.write("\n")

#zamknij deskryptor
fd.close()

print("Zakończono zapis\n")