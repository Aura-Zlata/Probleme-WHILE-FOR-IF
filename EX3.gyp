"""
Se dau numerele naturale m si n , unde m<n.
Sa se verifice daca n este o putere a lui m.
"""

import math 
m=int(input("Introdu m : "))
n=int(input("Introdu n : "))
if ((m>n)or(m==n)):
     print("nu corespunde conditiei")
else:
    l=round(math.log(n,m))
    if (m**l==n):
        print(n,"este o putere a lui",m)
    else:
        print(n,"nu este o putere a lui",m)