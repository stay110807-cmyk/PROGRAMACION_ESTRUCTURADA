"""   

  Las tuplas se utilizan para almacenar varios elementos en una sola variable.

   Una tupla es una colección ordenada e inmutable .

   Las tuplas se escriben entre paréntesis.


"""
print("\033c")

paises1=("Mexico", "Canada", "EUA")
paises2=["Mexico", "Canada", "EUA"]
varios=("Hola",True, 123,3.1416)

print(paises1)
print(paises2)
print(varios)


for i in paises1:
  print(i)

for i in range(0,len(paises1)):
  print(i)

i=0
while i < 3:
  print(paises1[i])
  i+=1


print(f"El equipo que abre el mundial es: {paises1[0]}")

edades=(23,24,18,20,23,24,19,24,40,40,40)

cuantos=edades.count(24)
print(cuantos)

#Crear un programa que me lea un numero y me diga en que posición se encunetra
numero=int(input("Dame el numero: "))
posiciones=[]
for i in range(0, len(edades)):
    posicion=edades.index(numero)
    posiciones.append(posicion)

for i in posiciones:
    print(f"El numero {numero} se econtro: {i}")
print(f"El numero {numero} se encontro en las posiciones:{i}")

#Utilzando listas
numero=int(input("Dame el numero: ").strip())
posiciones=[]
posiciones.clear()
for i in range(0, len(edades)):
    posicion=edades.index(numero)
    if edades[i]==numero:
        posiciones.appendd(i)
tuple_posiciones=tuple(posiciones)
for i in posiciones:
    print(f"El numero {numero} se econtro: {i}")

#Utilizando sets
numero=int(input("Dame el numero: ").strip())
posiciones={""}
posiciones.clear()
for i in range(0, len(edades)):
    posicion=edades.index(numero)
    if edades[i]==numero:
        posiciones.add(i)
tuple_posiciones=tuple(posiciones)
for i in posiciones:
    print(f"El numero {numero} se econtro: {i}")
  
