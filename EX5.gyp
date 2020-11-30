"""
Conform calendarului japonez, fiecare an poarta numele unui animal.
fiecare denumire se repeta o data la 12 ani.
Deci, un ciclu este format din 12 &ni cu urmatoarele denumiri de animale in aceasta ordine:
sobolan,bou,tigru,iepure,dragon,sarpe,cal,oaie,maimuta,cocos,caine,porc;
stiind a anul 2000 a fost anul Dragonului , sa se scrie un algoritm care va citi de la tastatura anul si va afisa denumirea lui conform calendarului japonez.
"""

a=eval(input("Introdu anul: "))
if (a//1000==0):
    print("Introdu alt an")
elif (a%12==0):
    print("Anul Maimutei")
elif (a%12==1):
    print("Anul Cucosului")   
elif (a%12==2):
    print("Anul Cainelui")
elif (a%12==3):
    print("Anul Porcului")
elif (a%12==4):
    print("Anul Sobolanului")
elif (a%12==5):
    print("Anul Boului")
elif (a%12==6):
    print("Anul Tigrului")
elif (a%12==7):
    print("Anul Iepurelui")
elif (a%12==8):
    print("Anul Dragonului")
elif (a%12==9):
    print("Anul Sarpelui")
elif (a%12==10):
    print("Anul Calului")
else:
    print("Anul Oaiei")