#Funkciju iz prethodne zadaće učitati kao funkciju modula u novi program i pozvati je nakon traženja unosa od korisnika
from zadaca6 import rekurzivno
def zadaca7(n):
    from zadaca6 import rekurzivno
    return n
n=input('pozovite funkciju! ')
a=zadaca7(n)
print('pozvana funkcija: ',a)
