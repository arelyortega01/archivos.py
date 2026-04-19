#arely ortega quiroz 

# Programa para calcular descuento en compras mayores a 500 pesos
compra = 1000.0  # dato fijo de ejemplo

if compra > 500 and not (compra <= 500):
    descuento = compra * 0.1  # 10% de descuento
    total = compra - descuento
    print("Tienes un descuento de:", descuento, "pesos")
    print("El total a pagar es:", total, "pesos")
else:
    print("No aplica descuento, el total es:", compra, "pesos")
