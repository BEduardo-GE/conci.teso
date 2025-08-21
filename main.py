#Ser un soporte digital para el área de Tesorería que permita realizar de forma más 
#eficiente los cierres de caja diarios, comparando montos del sistema con efectivo 
#físico, identificando faltantes o sobrantes por colaborador, y ayudando a ajustar el 
#fondo de caja a ₡40,000 de forma automatizada.

from entrada_datos import (ingreso_datos, fecha, monto_fondo)

from calculos import (suma_billetes, suma_monedas, suma_efectivo, total_reportado, total, resultado, metodos_pago)

def main (billetes, monedas, metodos_dict, ingreso_neto):
    caja, cajero = ingreso_datos ()
    fecha_corte = fecha ()
    fondo = monto_fondo ()
    total_billetes = suma_billetes (billetes)
    total_monedas = suma_monedas (monedas)
    total_efectivo = suma_efectivo (total_billetes, total_monedas)
    total_metodos = metodos_pago(metodos_dict)
    total_rep = total_reportado(total_efectivo, total_metodos) 
    total_final = total(total_rep, fondo)
    resultado_final = resultado(total_final, ingreso_neto)

    print("\n--- RESUMEN FINAL ---")
    print("Caja:", caja)
    print("Cajero:", cajero)
    print("Fecha:", fecha_corte.strftime("%d/%m/%Y"))
    print("Fondo:", fondo)
    print("Total billetes:", total_billetes)
    print("Total monedas:", total_monedas)
    print("Total efectivo:", total_efectivo)
    print("Total métodos de pago:", total_metodos)
    print("Total reportado:", total_rep)
    print("Total final (menos fondo):", total_final)
    print("Diferencia contra ingreso neto:", resultado_final)