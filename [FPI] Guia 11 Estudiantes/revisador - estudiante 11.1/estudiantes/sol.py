'''
import math
import random


def esc(text):
    with open("IO_Esperado.txt","w",encoding="utf-8") as a:
        a.write(text)
    return 
        

sol = ""

for _ in range(10):
    sol += "###ENTRADA###\n"

    num = random.randint(0,150)
    name = "tabla-" + str(num) + ".txt"
    
    
    
    sol += str(num)
    sol += "\n"
    sol += name
    sol += "\n"

    sol += "###SALIDA###\n"

    text = []
    for i in range(13):
        text.append( str(num) + " x " + str(i) + " = " + str(i*num) )

    text = "\n".join(text)
    sol += text
        
    sol += "\n"
sol = sol.strip()
esc(sol)


'''

num = int(input("Ingrese la tabla requerida: "))
name = input("Ingrese el nombre del archivo de salida:  ")
text = []
for i in range(13):
    text.append( str(num) + " x " + str(i) + " = " + str(i*num) )

text = "\n".join(text)
with open(name,"w") as a:
    a.write(text)
    

