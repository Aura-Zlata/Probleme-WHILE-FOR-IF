"""
Sa se calculeze 1!+2!+3!+...+n!(n>1)
"""

n=int(input("Introduceti numarul: "))
s=0
for i in range(1,i+1):
    p=1
    for n in range(1,i+1):
        p*=n
    s+=p
print("1!+2!+3!+...+n!=",s)
