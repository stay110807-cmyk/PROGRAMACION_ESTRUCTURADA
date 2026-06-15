print("\033c")

#Ejemplo 1 Crear una lista de numeros e imprimir el contenido
numeros=[23,23,45,8,24,0,100]
print(numeros)
lista="["
for i in numeros:
    lista=lista+str(i)+", "
    lista+=f"{i},"
print(lista+"]")

lista="["
for i in range(0,len(numeros)):
    lista+=f"{numeros[i]},"
print(lista+"]")

lista="["
i=0
while i < len(numeros):
    lista+=f"{numeros[i]},"
    i += 1
print(lista+"]")


#Ejemplo 2 Crear una lista de palabras y posteriormente buscar la coincidencia de una palabra 
#1ER FORMA
palabras=["UTD","tercer","cautrismestre","TI"]
palabra=input("Dame la palabra a bsucar: ").strip()
if palabra in palabras:
    print(f"encontre la palabra {palabra} en la lista")
else:
    print(f"No encontre la palabra {palabra} en la lista")

#2DA FORMA
palabras=["UTD","tercer","cautrismestre","TI"]
palabra=input("Dame la palabra a bsucar: ").strip()
encontro=False 
for i in palabras:
    if i==palabra:
        encontro=True
    else:
        encontro=False
if encontro:
    print(f"encontre la palabra {palabra} en la lista")
else:
    print(f"No encontre la palabra {palabra} en la lista")
        
#3er FORMA
palabras = ["UTD", "tercer", "cuatrimestre", "TI"]

palabra = input("Dame la palabra a buscar: ").strip()

encontro = False

for i in range (0, len(palabras)):
    if palabras[i]==palabra:
        encontro = True
if encontro:
    print(f"Palabra: {palabra}")
else:
    print("No encontrado")

#Ejemplo 3 Añadir elementos a la lista
lista=[]
#opcion 1
true=True
while true:
    valor=input("Dame un valor: ").strip()
    lista.append(valor)
    true=input("Ingresa true/false para continuar: ").strip()
    if true != "true":
        true=False
print(lista)

#opcion 2
opc="true"
while opc=="true":
    valor=input("Dame un valor: ").strip()
    lista.append(valor)
    opc=input("Ingresa True/False para continuar: ").strip().lower()
print(lista)

#Ejemplo 4 Crear una lista multidimensional que permita almacenar el nombre y telefono de una agenda
print("\033c")
agenda=[
            ["carlos","6182552336"],
            ["Adrian","6182556974"],
            ["Luis","6185224785"]
        ]

print(agenda)

for i in agenda:
    print(i)

for r in range(0,3):
    for c in range(0,2):
        print(agenda[r][c])

lista=""
for r in range(0,3):
    for c in range(0,2):
        lista+=f"{agenda[r][c]}, "
    lista +="\n"
print(lista)