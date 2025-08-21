# seguia al usuario para que este pueda desarrollar de manera ordenada

import datetime
import time
from main import main
def ingreso_datos (): 
    caja = int(input("ingrese el numero de caja: \t"))
    cajero = input(" ingrese el nombre del cajero: \t")
    time.sleep(2)
    return caja, cajero 

def fecha():
    while True:
        entrada = input("ingrese la fecha en formato dd/mm/aaaa: \t")
        try:
            # usando datatime para validar el formato de fecha
            fecha_dt = datetime.datetime.strptime(entrada, "%d/%m/%Y")
            print("Fecha válida:", fecha_dt)
            return fecha_dt
        except ValueError:
            print("Formato de fecha inválido. Por favor use dd/mm/aaaa.")
            time.sleep(2)

def monto_fondo ():
    while True:
        try:
            fondo = float(input("Ingrese el monto del fondo: \t"))
            if fondo > 0 and fondo < 1000000:
                return fondo
            else:
                print("El monto del fondo debe ser mayor a 0 y menor a 1000000")
        except ValueError:
            print("Por favor ingrese un número válido para el monto del fondo.")
            time.sleep(2)

# Inicializar variables antes del ciclo principal
billetes = {}
monedas = {}
metodos_pago = {}
ingreso_neto = 0

while True:
    print("1. Ingreso de billetes")
    print("2. Ingreso de monedas")
    print("3. Ingreso de métodos de pago")
    print("4. Guardar y salir")
    opcion = input("Seleccione una opción: \t")
    match opcion:
        case "1":
            while True:
                billetes = {}
                print("\n--- Ingreso de billetes ---")

                try:
                    billetes["50000"] = float(input("Ingrese el monto de 50000: \t"))
                    billetes["20000"] = float(input("Ingrese el monto de 20000: \t"))
                    billetes["10000"] = float(input("Ingrese el monto de 10000: \t"))
                    billetes["5000"]  = float(input("Ingrese el monto de 5000: \t"))
                    billetes["2000"]  = float(input("Ingrese el monto de 2000: \t"))
                    billetes["1000"]  = float(input("Ingrese el monto de 1000: \t"))

                    # Validar que todos los montos sean >= 0 lo que significa ¿Algún monto ingresado es menor que cero?
                    if any(monto < 0 for monto in billetes.values()): # verifica si hay montos negativos, es un tipo bucle.
                        print(" El monto de los billetes no puede ser negativo. Intente de nuevo.\n")
                        continue  # vuelve a pedir todos los billetes

                    print("\n Billetes ingresados correctamente:")
                    for denom, monto in billetes.items():
                        print(f"₡{denom}: {monto}")
                    break  # sale del while si todo está correcto
                except ValueError:
                    print("Error: Ingrese solo valores numéricos.")
        case "2":
            while True:
                monedas = {}
                print("\n--- Ingreso de monedas ---")

                try:
                    monedas["500"] = float(input("Ingrese el monto de 500: \t"))
                    monedas["100"]  = float(input("Ingrese el monto de 100: \t"))
                    monedas["50"]  = float(input("Ingrese el monto de 50: \t"))
                    monedas["25"]  = float(input("Ingrese el monto de 25: \t"))
                    monedas["10"]   = float(input("Ingrese el monto de 10: \t"))
                    monedas["5"]   = float(input("Ingrese el monto de 5: \t"))

                    # Validar que todos los montos sean >= 0
                    if any(monto < 0 for monto in monedas.values()) :  # verifica si hay montos negativos, es un tipo bucle.
                        print(" El monto de las monedas no puede ser negativo. Intente de nuevo.\n")
                        continue
                except ValueError:
                    print("Erro de ingreso.")
        case "3":
            while True:
                metodos_dict = {}
                print("\n--- Ingreso de métodos de pago ---")
                try:
                    metodos_dict["Efectivo"] = float(input("Ingrese el monto en efectivo: \t"))
                    metodos_dict["Tarjeta"]  = float(input("Ingrese el monto con tarjeta: \t"))
                    metodos_dict["Transferencia"] = float(input("Ingrese el monto por transferencia: \t"))
                    metodos_dict["Compra click"] = float(input("Ingrese el monto con compra click: \t"))
                    metodos_dict["Otros"] = float(input("Ingrese el monto con crédito: \t"))

                    if any(monto < 0 for monto in metodos_dict.values()):
                        print("El monto no puede ser negativo.\n")
                        continue

                    # ✅ Aquí capturás el ingreso neto
                    ingreso_neto = float(input("Ingrese el monto de ingresos netos del sistema: \t"))

                    # Asignar metodos_dict a metodos_pago para usarlo fuera del case
                    metodos_pago = metodos_dict

                    print("\n Métodos de pago ingresados correctamente:")
                    for metodo, monto in metodos_dict.items():
                        print(f"{metodo}: ₡{monto}")
                    break
                except ValueError:
                    print("Error: Ingrese solo valores numéricos.")
                    print("\n Métodos de pago ingresados correctamente:")
                    for metodo, monto in metodos_dict.items():
                        print(f"{metodo}: ₡{monto}")
                    break
                except ValueError:
                    print("Error: Ingrese solo valores numéricos.")

        case "4":
            print("Guardando datos y saliendo...")

            # Validar si los datos están completos
            if not billetes or not monedas or not metodos_pago or ingreso_neto == 0:
                print("\n❌ Faltan datos. Asegúrese de ingresar billetes, monedas, métodos de pago e ingreso neto antes de continuar.")
                continue

    main(billetes, monedas, metodos_pago, ingreso_neto)
    break




