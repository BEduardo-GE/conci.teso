
def suma_billetes(ingreso_billetes):
    if not isinstance(ingreso_billetes, (list, tuple)):
        raise ValueError("ingreso_billetes debe ser una lista o tupla")
    return sum(ingreso_billetes)

def suma_monedas(ingreso_monedas):
    return sum(ingreso_monedas)

def suma_efectivo(total_billetes, total_monedas):
    return total_billetes + total_monedas

def metodos_pago(BAC, sinpe, entrega_parcial):
    return BAC + sinpe + entrega_parcial
 
def total_reportado(billetes_total, monedas_total):
    return billetes_total + monedas_total 

def total(total_reportado, monto_fondo ):
    return total_reportado - monto_fondo

def resultado(total_reportado, ingreso_neto):
    diferencia = total_reportado - ingreso_neto
    if diferencia > 0:
        print(f"sobrante de : {diferencia} colones")
    elif diferencia < 0:
        print(f"faltante de : {abs(diferencia)} colones")
    else:
        print("no hay diferencia.")
        
    return diferencia


#metodos_total