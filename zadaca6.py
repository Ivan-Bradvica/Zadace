#Napisati rekurzivnu funkciju koja kao parametar prima string,
#a kao rezultat taj string ispisuje sa zada.

def rekurzivno(x):
    return (x[::-1])
unos=input("unesite string")
x=rekurzivno(unos)
print(x)
