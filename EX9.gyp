"""
Un numar natural se numeste numar perfect daca este egal cu suma divizorilor lui, in afara de el insusi.
De exemplu, 6 este numar perfect, deoarece 6=1 +2 + 3.
Sa se afle numerele perfecte mai mici decit numarul natural dat n.
"""
n=int(input("Introduceti nr: "))
for a in range(1,n):
    b=0
    for i in range(1,a):
        if (a%i==0):
            b+=i
    if b==a:
        print(a,end=" ")
