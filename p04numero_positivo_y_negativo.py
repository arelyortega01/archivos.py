#arely ortega quiroz 

# Programa para saber si un número es positivo o negativo
num = 5  # dato fijo de ejemplo

if num > 0 and not (num < 0):
    print("El número es positivo")
elif num < 0 or not (num > 0):
    print("El número es negativo")
else:
    print("El número es cero")
