#Koristeći listu imena iz prethodnog zadatka svakom studentu generirati nasumičnu ocjenu od 1 do 5.
#Prebrojati u rječnik koliko ima kojih ocjena.
#Izračunati postotak prolaznosti. (sve ocjene veće od 1)

from random import*
lista_imena=['Josip', 'Ivan', 'Ivan', 'Josip', 'Ivan', 'Ivan', 'Katarina', 'Božena', 'Ivona', 'Marija', 'Josipa', 'Marko', 'Dario', 'Mihael',
'Stana', 'Bruno', 'Anamarija', 'Andrea', 'Petar', 'Marko', 'Amnesa', 'Nikola', 'Antonela', 'Leon', 'Ivan', 'Ante', 'Ivan',
'Jure', 'Jan', 'Florijan', 'Boris', 'Ivan', 'Stipe', 'Damir', 'Ana', 'Tin', 'Iva', 'Kristina', 'Josip', 'Tomislav', 'Luka', 'Ivan',
'Martin', 'Marko', 'Ante', 'Nikolina', 'Ivan', 'Toni', 'Ante', 'Darija', 'Dominik', 'Lucija', 'Luka', 'Ana', 'Emanuel',
'Petar', 'Matej', 'Stjepan', 'Josip', 'Luka', 'Marija', 'Toni', 'Iva ', 'Perica', 'Antonio', 'Ante', 'Marijan', 'Mario',
'Antonio', 'Stipe', 'Filip', 'Ivan', 'Ivan', 'Luka', 'Ante Bruno', 'Ivan', 'Vinko', 'Ivan', 'Matijas', 'Ivan', 'Freda', 'Kristina',
'Josip', 'Lucija']

rjecnik={}
nedovoljan=0
dovoljan=0
dobar=0
vrlo_dobar=0
odlican=0
suma=0
prolazno=0
for i in lista_imena:
    rjecnik[i]=randint(1,5)
    
for k,v in rjecnik.items():
    if v==1:
        nedovoljan+=1
    if v==2:
        dovoljan+=1
    if v==3:
        dobar+=1
    if v==4:
        vrlo_dobar+=1
    if v==5:
        odlican+=1
prolazno=dovoljan+dobar+vrlo_dobar+odlican
suma=nedovoljan+dovoljan+dobar+vrlo_dobar+odlican
prolazna_ocjena=prolazno/suma
print("nedovoljnih ima: ", nedovoljan)
print("dovoljnih ima: ", dovoljan)
print("dobrih ima: ", dobar)
print("vrlo dobrih ima: ", vrlo_dobar)
print("odlicnih ima: ", odlican)
print("prolaznost iznosi: ", round(prolazna_ocjena*100,2),"%")
exit=input("pritisnite neko slovo za izlaz")