#Maria Jose Castro 181202
#Roberto Figueroa 18306
#Diana de Leon 18607

#Ejercicio 1
#paquetes necesarios
import math
import itertools

def genElements(n):
    return list(range(n))
    

mensaje = "1.Orden-Sin reemplazo\n2.Orden-Con remplazo\n3.Sin orden-sin remplazo\n4.Sin orden-con remplazo\n5.Salir"
opcion = 0
opcion= int(input("\nMenu \n"+ mensaje + "\n" + "Ingrese una opcion del menu: "))
while opcion != 5:
    n = int(input("\nIngrese el numero de elementos: "))
    r = int(input("\nIngrese el numero de elementos de la muestra: "))
    
    resultado = 0
    perm = []
    if opcion == 1:
        resultado = math.factorial(n) / math.factorial((n-r))
        perm = itertools.permutations(genElements(n),r)
    elif opcion == 2:
        resultado = n ** r
        perm = itertools.product(genElements(n),genElements(n))     
    elif opcion == 3:
        resultado = math.factorial(n) / (math.factorial(r)* math.factorial((n-r)))
        perm = itertools.combinations(genElements(n),r)
    elif opcion == 4:
        resultado = math.factorial((r+n-1)) / (math.factorial(r)* math.factorial((n-1)))
        perm = itertools.combinations_with_replacement(genElements(n),r)
    else:
        print("Opcion no valida")
    print("La cantidad es : " + str(int(resultado)))
    print("Las combinaciones/permutaciones son: ")
    print(list(perm))

    opcion= int(input("\nMenu \n"+ mensaje + "\n" + "Ingrese una opcion del menu: "))







