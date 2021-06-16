import re 
#
email=input("Unesite e-mail adresu: ")
reg="(^[a-zA-Z].*)([a-zA-Z])@fpmoz.sum.ba$"
kraj=re.match(reg,email)
while True:
    if kraj:
       print("Tocan email. ")
       break
    else:
       print("Netocan email.")
       input("Netocna email adresa, unsite ponovo: ")
       if input:
           print("Unjeli ste tocna email")
           break   
       

edu_ID=input("Unesite eduID: ")
reg_2="^([a-zA-Z])([a-zA-Z].*)[0-9]*@sum.ba$"
kraj_2=re.match(reg_2,edu_ID)

while True:
    if kraj_2:
       print("Tocan eduId. ")
       break
    else:
       print("Netocan eduID.")
       input("Netocan eduID, unsite ponovo: ")
       if input:
           print("Unjeli ste tocan eduID")
           break   

print("Vaš email je: ",email," i vaš eduID je: ",edu_ID)
       
        