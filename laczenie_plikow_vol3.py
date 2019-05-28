# -*- coding: utf-8 -*-

import fnmatch
import os


def pobierz_dane0(plikcsv):                             # odczytujemy plik z naglowkami
    """
    Aplikacja ma otworzyć i zapisac do listy nagłówek (10 pierwszych wierszy)
    """
    dane = []  # deklarujemy pusta liste
    if os.path.isfile(plikcsv):  # sprawdzamy czy plik istnieje na dysku
        with open(plikcsv, "r") as zawartosc:  # otwieramy plik do odczytu
            licz = 8
            for linia in zawartosc:
                if licz > 0:        # sprawdzamy pierwsze 8 linii (nagłówek) i wykonujemy poniższe operacje
                    linia = linia.replace("\n", "")     # usuwamy znaki konńca lini
                    linia = linia.replace("\r", "")     # usuwamy znaki konca lini
                    linia = linia[:-1]                  # usuwamy znak ";" z końca linii
                    linia = linia.replace("utf-8", "")  # odczytujemy znaki jako utf-8
                    dane.append(linia)
                    licz -= 1
        zawartosc.close()
    else:
        print("Plik z danymi: ", plikcsv, " nie istnieje!")
    return dane

##################################################################################################
##################################################################################################


def pobierz_dane1(plikcsv):                             # odczytujemy plik bez naglowkow
    """
    Aplikacja ma otworzyć i zapisać zawartość zadeklarowanego pliku z wyłączeniem nagłówków do listy
    """
    dane = []                                           # deklarujemy pusta liste
    if os.path.isfile(plikcsv):                         # sprawdzamy czy plik istnieje na dysku
        with open(plikcsv, "r") as zawartosc:           # otwieramy plik do odczytu
                                                        # w python > 3.5 potrzeba kodowania line-1
                                                        # do rozkodowania znaku stopni Celcjusza
            for i in range(0, 8):
                zawartosc.readline()
                       
            for linia in zawartosc:
                linia = linia.replace("\n", "")         # usuwamy znaki konńca lini
                linia = linia.replace("\r", "")         # usuwamy znaki konca lini
                linia = linia[:-1]                      # usuwamy znak ";" z konca linii
                linia = linia.replace("utf-8", "")      # odczytujemy znaki jako utf-8

                rok = linia[6:10]                       # na potrzeby zleceniodawcy zmieniamy format daty
                miesiac = linia[3:5]
                dzien = linia[0:2]
                z_data = linia.replace(linia[0:10], rok + '-' + miesiac + '-' + dzien)

                dane.append(z_data)
        zawartosc.close()
    else:
        print("Plik z danymi: ", plikcsv, " nie istnieje!")
    return dane

#################################################################################################
#################################################################################################


szukamy = input('Podaj fragment nazwy plikow, ktore chcemy polaczyc (np: 102017): ')
pliki = [x for x in os.listdir(".") if fnmatch.fnmatch(x, "*"+szukamy+".CSV")]  # przypisujemy nazwy szukanych plików do listy
if not pliki:
    print("Brak plikow w przeszukiwanym katalogu")

pliki.sort()                                                  # sortujemy
plik0 = pliki[0]                                              # zapisujemy w zmiennej pierwszy element z listy plików
out = input("Podaj nazwe pliku wyjsciowego lacznie z rozszerzeniem: ")
lines0 = pobierz_dane0(plik0)                                  # przypisujemy listę zawierającą nagłówki do zmiennej

out0 = open(out, "a+")                                        # otwieramy plik do ktorego bedziemy zapisywac dane
for line0 in lines0:                                           # zapisujemy wiersze zawierające informację o nagłówkach
    out0.writelines(line0)
    out0.write("\n")
out0.close()
print("Nagłówki zostały wczytane")

for plik in pliki:
    pomiary = pobierz_dane1(plik)       # odczytujemy wszystkie pliki z pominieciem nagłówków
    out0 = open(out, "a+")              # "a+" daje mozliwosc dopisywania do pliku
    for pomiar in pomiary:              # każdą linię z danymi przepisujemy do wcześniej utworzonego pliku
        out0.writelines(pomiar)
        out0.write("\n")
    out0.close()
print("Pliki zostały polaczone")
