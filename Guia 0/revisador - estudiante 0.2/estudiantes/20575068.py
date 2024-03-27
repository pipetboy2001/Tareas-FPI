import random
random.seed(21)
lista = []
for i in range(1,22):
    num = str(i)
    lista.append("0"*(2-len(num))+num)
random.shuffle(lista)

print("Elija un número entero del 1 al 21.")

i=0
while i<3:
    lista1 = []
    lista2 = []
    lista3 = []

    while len(lista)>0:
        lista1.append(lista.pop(0))
        lista2.append(lista.pop(0))
        lista3.append(lista.pop(0))

    print()
    print("Grupo 1: ",lista1)
    print("Grupo 2: ",lista2)
    print("Grupo 3: ",lista3)
    op = input("Indique en qué grupo está su número (1, 2 o 3): ")

    if op == "1":
        lista = lista2 + lista1 + lista3
    elif op == "2":
        lista = lista1 + lista2 + lista3
    else:
        lista = lista2 + lista3 + lista1
    i+=1

print("Su número es: ",lista[10])