# seguia al usuario para que este pueda desarrollar de manera ordenada

import datetime
import time
def ingreso_datos (): 
    caja = int(input("ingrese el numero de caja: \t"))
    cajero = input(" ingrese el nombre del cajero: \t")
    time.sleep(2)
    return caja, cajero 

def fecha():
    while True:
        entrada = input("ingrese la fecha en formato dd/mm/aaaa: \t")
        try:
            # Aquí va el código que deseas intentar, por ejemplo:
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

def ingreso_billetes ():
    return [
        float(input("ingrese el monto de 20000: \t")),
        float(input("ingrese el monto de 10000: \t")),
        float(input("ingrese el monto de 5000: \t")),
        float(input("ingrese el monto de 2000: \t")),
        float(input("ingrese el monto de 1000: \t"))
    ]

def ingreso_monedas():
    moneda_500 = float(input("ingrese el monto en monedas de 500: \t"))
    moneda_100 = float(input("ingrese el monto en monedas de 100: \t"))
    moneda_50 = float(input("ingrese el monto en monedas de 50: \t"))
    moneda_25 = float(input("ingrese el monto en monedas de 25: \t"))
    moneda_10 = float(input("ingrese el monto en monedas de 10: \t"))
    moneda_5 = float(input("ingrese el monto en monedas de 5: \t"))
    time.sleep(2)
    return [moneda_500, moneda_100, moneda_50, moneda_25, moneda_10, moneda_5]

def ingreso_metodos_pago():
    print(" Ingresos electrónicos y parciales:")
    BAC = float(input("Monto BAC (tarjeta): "))
    SINPE = float(input("Monto SINPE: "))
    entrega_parcial = float(input("Entregas parciales: "))
    return BAC, SINPE, entrega_parcial

def ingresos_nets():
    ingresos_net = float(input("ingresos netos: \t"))
    time.sleep(1)
    return ingresos_net


"""
monto_20000 = float(input("ingrese el monto de 20000: \t"))
    monto_10000 = float(input("ingrese el monto de 10000: \t"))
    monto_5000 = float(input("ingrese el monto de 5000: \t"))
    monto_2000 = float(input("ingrese el monto de 2000: \t"))
    monto_1000 = float(input("ingrese el monto de 1000: \t"))
    time.sleep(2)
"""