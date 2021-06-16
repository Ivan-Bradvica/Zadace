import re
var=str(input("Unesite string: "))
var=var.lower()
regex="^i.*[0-5]\rs.*b$"
rezultat=re.findall(regex,var)
if rezultat:
    print("Podudaranje")
else:
    print("Nema podudaranja")