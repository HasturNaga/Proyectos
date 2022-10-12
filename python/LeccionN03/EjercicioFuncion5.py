# Ejercicio 5: calculadora de impuestos.
# Crear una funcion para calcular el total de un pago incluyendo
# un impuestoaplicado. (IVA)
# Formula: pago_tota = pago_sin_impuestos + pago sin impusto * (impuesto/100)
# Proporcione el pago sin impuesto: 1000
# Proporcione el monto del impuesto: 21%
# Pago con impuesto: xxxxx

# Creamos la funcion que calcula el total del pago incluyendo el impuesto.
def calcular_total_pago(pago_sin_impuesto, impuesto):
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
    return pago_total

pago_sin_impuesto = float(input('Digite el pago sin impuestos: '))
impuesto = float(input('Digite el monto del impuesto a aplicar: '))
pago_con_impuesto = calcular_total_pago (pago_sin_impuesto, impuesto)
print(f'El pago de impuesto es: {pago_con_impuesto}')