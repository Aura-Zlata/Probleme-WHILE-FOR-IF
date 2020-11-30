"""
Se da numarul natural n,n partine lui {28,29,30,31} 
Sa se afiseze denumirile lunilor cu numarul de zile n.
De exemplu, pentru n=30, se va afisa: aprilie;iunie;septembrie;noiembrie.
"""

n=int(input("Introduceti numarul: "))
if ((n<28)or(n>31)):
    print("Nu sunt luni cu asa numar de zile")
elif n==28:
    print("Februarie, daca nu e an bisect")
elif n==29:
    print("Februarie, daca e an bisect")
elif n==30:
    print("Aprilie,Iunie,Septembrie,Noiembrie")
else:
    print("Ianuarie,Martie,Mai,Iulie,August,Octombrie,Decembrie")
