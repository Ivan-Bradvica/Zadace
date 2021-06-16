"""Definirati dvije funkcije koje kao parametar primaju ime ali vraćaju različitu poruku dobrodošlice.
Jedna neka ispisuje “Pozdrav {ime}!”, a druga “Dobrodošao {ime}!”
Jedna od funkcija neka bude definirana lambda izrazom, a druga standardnim načinom.
Zatim definiraj treću funkciju koja kao parametar prima naziv funkcije za ispis dobrodošlice i poziva je tako
što pošalje vaše ime u nju.
Pozvati treću funkciju prosljeđujući joj neku od prve dvije definirane funkcije."""

def prva_funkcija(ime):
    return "Pozdrav " + ime

unos = input("Unesite ime: ")
print(prva_funkcija(unos))

druga = lambda ime: "Dobrodošao " + ime
print(druga("Ivan"))

def treca_funkcija(prva_funkcija):
    return prva_funkcija(unos)

print(treca_funkcija(prva_funkcija))

    
