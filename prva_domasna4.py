"""Напишете програма која ќе прочита два броја од корисникот и ќе го испечати збирот на броевите помеѓу нив што се делливи со 4."""

a = int(input("Vnesete broj: "))
b = int(input("Vnesete drug broj: "))
zbir = 0
for i in range(a,b+1):
    if i%4==0:
        zbir = zbir + i
print(zbir)