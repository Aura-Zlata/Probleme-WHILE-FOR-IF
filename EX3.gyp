"""
Se dau numerele naturale m si n , unde m<n.
Sa se verifice daca n este o putere a lui m.
"""

from math import log
m=int(input("Introdu nr m: "))
n=int(input("Introdu nr n: "))
a=log(n,m)
b=int(a)
if a-b==0:
     print("nr n este putere a lui m")
else:
     print("nr n nu este putere a lui m")
