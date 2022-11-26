
from heapq import *
d = {}

d["ana"] = 30
d["belu"] = 1

def func(d):
    d["hahaha"] = 10000

print(d)
func(d)
print(d)

class Test:

    def __init__(self,x) -> None:
        self.x = x


a = []
heappush(a,(100,Test(1),"ana"))
heappush(a,(30,Test(2),"dana"))
heappush(a,(3,Test(3),"cana"))
# a = [(100,Test(1),"ana"),(30,Test(2),"dana"),(3,Test(3),"cana")]

print(heappop(a)[2])
print(heappop(a)[2])
print(heappop(a)[2])

b = []
heappush(b,(100,Test(1)))
heappush(b,(20,Test(2)))
heappush(b,(1,Test(3)))

referinta_primul = b[0][1]
print("Referinta primul",referinta_primul.x)

print(heappop(b))
print("Referinta primul",referinta_primul.x)

print(heappop(b))
print("Referinta primul",referinta_primul.x)

print(heappop(b))
## DAR DUPA CE LE COMPARA HEAPUL?

## Trebuie sa fie tupluri in care prima e prioritatea

## E GRESIT SA ITEREZI PESTE UN HEAP ASA

## face referinta la ce era in primul element al heapului si deci direct la ala nu tine referinta ca in c la incputul vectorului
## orice ar fi acolo
print("\n\n\n\n")

a = []
heappush(a,(100,Test(1),"ana"))
heappush(a,(30,Test(2),"dana"))
heappush(a,(20,Test(3),"cana"))
heappush(a,(900,Test(3),"xxx"))
heappush(a,(0,Test(3),"yyy"))

print(nsmallest(3,a)[1:])
print(a)
print("12312312")
for x in a:
    print(x,type(x))

def test(lista):
    lista += [3]

X = [1,2,3]
test(X)
print(X)