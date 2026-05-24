"""Elaborar un algoritmo que permita leer los datos de un atumovil: marca, origen y costo;
imprimir el impuesto a pagar y el precio de venta incluyendo el impuesto. Considerar
lo siguiente: si el origen es "Alemania" tiene un impuesto del 20%, si es "Japon" tiene un 
impuesto del 30%, si es de "italia" tiene un impuesto del 15% y si es de "USA" es del 8%. Salir
del programa solo cunado el usuario ya no quiera ingresar más autos """

def borrarPantalla():
    print("\033c")
def ventaAutos(opcion, cont_autos, sum_total):
    borrarPantalla()
    

    while opcion == "S":
        #Entrada
        marca=input("Marca ").strip().upper()
        origen=input("Origen: ").strip().upper()
        costo=float(input("Costo: "))    
        impuesto=0 

        #proceso
        if origen == "ALEMANIA":
            impuesto=0.20
        elif origen == "JAPON":
            impuesto=0.30
        elif origen == "ITALIA":
            impuesto=0.15
        elif origen == "USA":
            impuesto=0.08
        else:
            impuesto=0

        impuesto_pesos=costo*impuesto
        pv=impuesto_pesos+costo

        #salida 
        print(f"El impuesto a pagar es: {impuesto_pesos}")
        print(f"El precio de venta es: {pv}")

        cont_autos =+ 1
        sum_total =+ pv
        opcion=input("Desea realizar de nuevo el proceso? (S/N)").upper().strip()
    return cont_autos,sum_total

CONT_AUTOS=0
SUM_TOTAL=0
OPCION="S"
cont_autos,sum_total=ventaAutos("S",0,0)    
print(f"El total de los vehiculos es: {cont_autos} \n EL monto total de los precios de venta {sum_total}")

ventaAutos()