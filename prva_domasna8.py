godina = int(input("Vnesete ja vasata godina: "))
if godina%4==0 and (godina%100!=0 or godina%400==0):
    print(f"{godina} e prestapna godina.")
else:
    print(f"{godina} ne e prestapna godina.")