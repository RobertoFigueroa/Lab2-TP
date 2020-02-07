#Maria Jose Castro 181202
#Roberto Figueroa 18306
#Diana de Leon 18607
import itertools
def genElements(n):
    return list(range(1,n+1))
    
tuplas = []
n=7
m=5
k=0
for i1 in range(1,n+1):
    for i2 in range(1,i1+1):
        for i3 in range(1,i2+1):
            for i4 in range(1,i3+1):
                for i5 in range(1,i4+1):
                    tuplas.append((i5,i4,i3,i2,i1))
                    k=k+1

perm = list(itertools.combinations_with_replacement(genElements(n),m))
print("El tamanio es de: " + str(k))


if len(perm) == len(tuplas):
    print("si son del mismo tamanio")
else:
    print("no son del mismo tamanio")

x = set(perm)
y = set(tuplas)



if x == y:
    print("Si tienen los mismos elementos")
else:
    print("No tienen los mismos elementos")

