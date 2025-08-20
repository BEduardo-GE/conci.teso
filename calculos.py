
def suma_billetes(billetes):
    return sum(billetes.values())

def suma_monedas(monedas):
    return sum(monedas.values())

def suma_efectivo(total_billetes, total_monedas):
    return total_billetes + total_monedas

def metodos_pago(metodos):
    return sum(metodos.values())
 
def total_reportado(total_efectivo, monedas_total):
    return total_efectivo + monedas_total 

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