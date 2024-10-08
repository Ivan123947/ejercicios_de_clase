#Escribe un programa que le pida al usuario que introduzca su año de nacimiento y calcule su edad actual.
# Asegúrate de que el programa solo permita el acceso a personas mayores de 18 años. 
# Si el usuario tiene menos de 18, el programa debe mostrar un mensaje indicando que no puede continuar. 
edad = int(input("¿que edad tienes?"))
if(edad>= 18):
    print("eres mayor de edad")
else:
    print("NO puedes continuar. eres menor")
    