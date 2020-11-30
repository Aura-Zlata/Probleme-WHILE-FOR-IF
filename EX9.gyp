"""
Un numar natural se numeste numar perfect daca este egal cu suma divizorilor lui, in afara de el insusi.
De exemplu, 6 este numar perfect, deoarece 6=1 +2 + 3.
Sa se afle numerele perfecte mai mici decit numarul natural dat n.
"""
n=int(input("Introduceti numarul: "))
for p in range(1,n):
    s=0
    for i in range(1,p):
        if (p%i==0):
            s+=i
    if s==p:
        print(p,end=" ")