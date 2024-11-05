#definimos funciones
def resta(a,b):
    resultado = a - b
    return resultado
print(resta(8,2))

def multiplicación (k, z):
    resultado = k * z
    return resultado
print(multiplicación(8,5))

def siguiente (num):
    resultado = num + 1
    return resultado
print(siguiente(10))

def mayor_de_dos (x, y):
    if (x > y):
        return x
    else:
        return y
print(mayor_de_dos(4,8))

def mayor_de_tres(x, y, z):
    if (x > y):
        if (x > z):
            return x
        else:
            return z
    else:
        if (y > z):
            return y
        else:
            return z
print (mayor_de_tres(5, 10, 13))

def mayor_de_cuatro (v1, v2, v3, v4):
    return mayor_de_tres(mayor_de_dos(v1,v2), v3, v4)
print(mayor_de_cuatro(3, 4, 5, 6))

def contar_vocales(texto):
    contador = 0
    for caracter in texto:
        if (caracter == 'o'):
            contador = contador + 1
        elif(caracter == 'e'):
            contador = contador + 1
        elif(caracter == 'i'):
            contador = contador + 1
        elif(caracter == 'a'):
            contador = contador + 1
        elif(caracter == 'u'):
           contador = contador + 1
    return contador
print(contar_vocales("hola mundo"))