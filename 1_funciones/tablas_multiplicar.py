'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- Sin estructuras de control
  2.- Sin funciones

'''
"""
#Limpiar pantalla
print("\033c")

#Entrada
numero1=int(input("Porfavor ingrese un numero: "))

#Proceso
resultado1=numero1 * 1
resultado2=numero1 * 2
resultado3=numero1 * 3
resultado4=numero1 * 4
resultado5=numero1 * 5
resultado6=numero1 * 6
resultado7=numero1 * 7
resultado8=numero1 * 8
resultado9=numero1 * 9
resultado10=numero1 * 10

#Salida
print(f"1 x {numero1}: {resultado1} \n2 x {numero1}: {resultado2} \n3 x {numero1}: {resultado3} \n4 x {numero1}: {resultado4} \n5 x {numero1}: {resultado5} \n6 x {numero1}: {resultado6} \n7 x {numero1}: {resultado7} \n8 x {numero1}: {resultado8} \n9 x {numero1}: {resultado9} \n10 x {numero1}: {resultado10}")
"""
'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- Con estructuras de control con for con decrementos de 10
  2.- Sin funciones

'''
"""
print("\033c")


tabla=int(input("Porfavor ingrese un numero para saber su tabla: "))

numero=1

for num in range (100,0,-10):
    multi=tabla *num
    print(f"{tabla} X {numero} = {multi}")
    numero += 1
"""
'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- Con estructuras de control con while con decrementos de 10
  2.- Sin funciones

'''

"""
tabla=int(input("POrfvaor ingrese un numero para saber su tabla: "))
    
numero = 100
while numero >= -10:
    multi=tabla*numero
    print(f"{tabla} X {numero} = {multi}")
    numero += 10
    """
    
"""
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- sin estructuras de control con while
  2.- con funciones

""" 
"""
def funciontabla_multiplicar():
  numero1=int(input("porfavor ingrese el numero del que quiere saber la tabla de multipicar: "))

  resultado1=numero1 * 1
  resultado2=numero1 * 2
  resultado3=numero1 * 3
  resultado4=numero1 * 4
  resultado5=numero1 * 5
  resultado6=numero1 * 6
  resultado7=numero1 * 7
  resultado8=numero1 * 8
  resultado9=numero1 * 9
  resultado10=numero1 * 10

  print(f"1 x {numero1}: {resultado1} \n2 x {numero1}: {resultado2} \n3 x {numero1}: {resultado3} \n4 x {numero1}: {resultado4} \n5 x {numero1}: {resultado5} \n6 x {numero1}: {resultado6} \n7 x {numero1}: {resultado7} \n8 x {numero1}: {resultado8} \n9 x {numero1}: {resultado9} \n10 x {numero1}: {resultado10}")

funciontabla_multiplicar()

"""

"""
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- sin estructuras de control con while
  2.- con funciones

""" 

num =1 
def tablaMultiplicar():
    tabla=int(input("Porfavor ingrese el numero del que quiere saber la tabla: "))
    for num in range (1,11):
        multi = tabla * num 
        print(f"{tabla} X {num} = {multi}")
        num +=1

tablaMultiplicar()