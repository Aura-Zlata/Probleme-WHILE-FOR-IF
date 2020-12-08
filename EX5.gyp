"""
Conform calendarului japonez, fiecare an poarta numele unui animal.
fiecare denumire se repeta o data la 12 ani.
Deci, un ciclu este format din 12 &ni cu urmatoarele denumiri de animale in aceasta ordine:
sobolan,bou,tigru,iepure,dragon,sarpe,cal,oaie,maimuta,cocos,caine,porc;
stiind a anul 2000 a fost anul Dragonului , sa se scrie un algoritm care va citi de la tastatura anul si va afisa denumirea lui conform calendarului japonez.
"""

a=eval(input("Introduceti anul: "))
if (a//1000==0):
    print("Introduceti alt an")
elif (a%12==0):
    print("al Maimutei")
elif (a%12==1):
    print("al Cucosului")   
elif (a%12==2):
    print("al Cainelui")
elif (a%12==3):
    print("al Porcului")
elif (a%12==4):
    print("al Sobolanului")
elif (a%12==5):
    print("al Boului")
elif (a%12==6):
    print("al Tigrului")
elif (a%12==7):
    print("al Iepurelui")
elif (a%12==8):
    print("al Dragonului")
elif (a%12==9):
    print("al Sarpelui")
elif (a%12==10):
    print("al Calului")
else:
    print("al Oaiei")
