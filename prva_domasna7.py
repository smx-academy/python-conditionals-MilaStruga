"""Напишете програма која ќе прочита големина на агли во триаголник, да се провери дали може да се формира триаголник со тие агли(збирот мора да биде 180) и
 ако може да се формира триаголник да се провери каков триаголник може да се формира"""

alfa = int(input("Vnesete agol na triagolnikot: "))
beta = int(input("Vnesete drug agol na triagolnikot: "))
gama = int(input("Vnesete tret agol na triagolnikot: "))
s = alfa + beta + gama
if s > 180:
    print("Ne postoi triagolnik so ovie agli.")
else:
    if alfa == 90 or beta == 90 or gama == 90:
        print("Triagolnikot e pravoagolen.")
    elif alfa > 90 or beta > 90 or gama > 90:
        print("Triagolnikot e tapoagolen.")
    else:
        print("Triagolnikot e ostroagolen.")