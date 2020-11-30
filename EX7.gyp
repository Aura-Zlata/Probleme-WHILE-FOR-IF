"""
Mihai are un unchi bogat care i a daruit in ziua cand s a nascut un dolar, iar in fiecare an urmator el dubla cadoul,si mai adauga atatia dolari cati ani implinea Mihai.
a).Sa se calculeze cati dolari a primit Mihai atunci cand a implinit n ani (n<20)
b).La ce varsta cadoul lui Mihai a fost mai mare de 100$
"""

n=int(input("Introdu numarul: "))
s=1
s2=1
h=0
for i in range(1,n+1):
    s=s*2+i
print("a)Cand Mihai a implinit",n,"ani, a primit",s,"dolari")
while s2<=100:
    h+=1
    s2=s2*2+h
print("b)Cadoul lui Mihai a fost mai mare de 100$, cand a implinit",h,"ani")