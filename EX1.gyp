"""
Se da numarul natural n,n partine lui {28,29,30,31} 
Sa se afiseze denumirile lunilor cu numarul de zile n.
De exemplu, pentru n=30, se va afisa: aprilie;iunie;septembrie;noiembrie.
"""

a=int(input("Introduceti nr: "))
if ((a<28)or(a>31)):
    print("Nu exista luni cu asa numar de zile")
elif a==28:
    print("Februarie, daca nu-i  an bisect")
elif a==29:
    print("Februarie, daca este an bisect")
elif a==30:
    print("Aprilie,Iunie,Septembrie,Noiembrie")
else:
    print("Ianuarie,Martie,Mai,Iulie,August,Octombrie,Decembrie")
