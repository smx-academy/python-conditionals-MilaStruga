"""Напишете програма која ќе прочита страни на правоаголник и квадрат, да се пресмета плоштината и да се провери дали збирот на плоштините е деллив со 2,3 или 5"""


a = int(input("Vnesete strana na pravoagolnik: "))
b = int(input("Vnesete druga strana na pravoagolnik: "))
c = int(input("Vnesete strana na kvadrat: "))
P_pravoagolnik = a*b
P_kvadrat = c*c 
zbir_p = P_pravoagolnik + P_kvadrat
print(f"Plostinata na pravoagolnikot e {P_pravoagolnik}")
print(f"Plostinata na kvadratot e {P_kvadrat}")
if zbir_p%2==0:
    print("Zbirot na plostinite e deliv so 2.")
else:
    print("Zbzirot na plostinite ne e deliv so 2.")
if zbir_p%3==0:
    print("Zbirot na plostinite e deliv so 3.")
else:
    print("Zbzirot na plostinite ne e deliv so 3.")
if zbir_p%5==0:
    print("Zbirot na plostinite e deliv so 5.")
else:
    print("Zbzirot na plostinite ne e deliv so 5.")
