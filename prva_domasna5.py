"""Напишете програма која ќе прочита два броја од корисникот и ќе го испечати производот на броевите, да се провери дали резултатот е парен или не парен."""

a = int(input("Vnesete broj: "))
b = int(input("Vnesete drug broj: "))
proizvod = a*b
if proizvod%2==0:
    print("Proizvodot e paren. ")
else:
    print("Proizvodot e neparen.")