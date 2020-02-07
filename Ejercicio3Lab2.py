import math
import itertools

def genElements(n):
    return list(range(1,n+1))


numeros= [1,2,3,4,5,6]
r=4 #cantidad de tiros
n=6 #caras del dado
#problema a
print("---------INCISO A----------------\n")
print("-->Los resultados posibles lanzando el dado 4 veces son "+ str(n**r) + " \n")


#problema b
# perm=list(itertools.permutations(genElements(n),r))
print("---------INCISO B----------------\n")

perm = list(itertools.product(numeros, repeat=4))


counter = 0
for i in perm:
    register = 0
    for j in i:
        register = register + j
    if register == 18:
        counter += 1
print("-->Las tuplas que suman 18 son : " + str(counter) + "\n")


#problema c
#calculo seleccionado
print("---------INCISO C----------------\n")

sum =[]
dict = {}

for i in perm:
    register = 0
    for j in i:
        register = register + j
    sum.append(register)

for i in range(4,25):
    dict[i] = sum.count(i)

print("-->La suma maxima orenada es : \n" + str(dict))
print("-->Siendo 14 el maximo numero:  " + str(dict[14])  )