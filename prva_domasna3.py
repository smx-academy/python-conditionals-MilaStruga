"""Напишете програма која ќе прочита број од корисникот и ќе го провери дали тој е парен, и потоа ќе испечати соодветната порака."""

a = int(input("Vesete broj: "))
if a%2==0:
    print(f"Brojot {a} e paren.")
else:
    print(f"Brojot {a} ne e paren.")