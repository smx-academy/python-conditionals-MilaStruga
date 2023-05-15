"""Напишете програма која ќе прочита број од корисникот и ќе го провери дали тој е деллив со 3, 5, 3 и 5, а потоа ќе испечати соодветната порака."""

a = int(input("Vnesete broj: "))
if a%3==0:
    print(f"Brojot {a} e deliv so 3.")
else:
    print(f"Brojot {a} ne e deliv so 3.")
if a%5==0:
    print(f"Brojot {a} e deliv so 5.")
else:
    print(f"Brojot {a} ne e deliv so 5.")