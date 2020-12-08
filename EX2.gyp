"""
Sa se calculeze 1!+2!+3!+...+n!(a>1)
"""

a=int(input("Introduceti nr: "))
s=0
for i in range(1,a+1):
    p=1
    for a in range(1,i+1):
        p*=a
    s+=p
print("1!+2!+3!+...+n!=",s)
