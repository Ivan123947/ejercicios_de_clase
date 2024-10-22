#pedir al usuario por el número de la tabla
num_tabla = int
indice = 1
resultado = int
print("dime el número de la tabla de multiplicar")
num_tabla = int(input())
while (indice < 11):
    resultado = num_tabla * indice
    print(indice, "x", num_tabla, "=", resultado)
    indice = indice +1
print("fin")
