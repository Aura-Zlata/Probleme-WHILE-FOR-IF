"""
Mihai are un unchi bogat care i a daruit in ziua cand s a nascut un dolar, iar in fiecare an urmator el dubla cadoul,si mai adauga atatia dolari cati ani implinea Mihai.
a).Sa se calculeze cati dolari a primit Mihai atunci cand a implinit n ani (c<20)
b).La ce varsta cadoul lui Mihai a fost mai mare de 100$
"""

c=int(input("Introduceti nr: "))
s=1
s2=1
d=0
for i in range(1,c+1):
    s=s*2+i
print("a)Cand Mihai a implinit",c,"ani, a primit",s,"$")
while s2<=100:
    d+=1
    s2=s2*2+d
print("b)Cadoul lui Mihai a fost mai mare de 100$, la varsta de",d,"ani")