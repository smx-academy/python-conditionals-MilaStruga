"""Напишете програма која ќе прочита два броја од корисникот и ќе го испечати збирот, разликата, производот и количникот на двата броја. 
Споредете кој резултат е поголем, збирот или производот"""

a = int(input("Vnesete broj: "))
b = int(input("Vnesete drug broj: "))
zbir = a+b
print(zbir)
razlika = a-b
print(razlika)
proizvod = a*b
print(proizvod)
kolicnik = a/b
print(kolicnik)
if zbir > proizvod:
    print("Zbirot e pogolem od proizvodot.")
else:
    print("Proizvodot e pogolem od zbirot.")