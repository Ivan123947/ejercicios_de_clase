#Escribe un programa que le pida al usuario ingresar un nombre de usuario y una contraseña. 
# Si el nombre de usuario es "admin" y la contraseña es "1234", el programa debe mostrar "Acceso concedido". Si no, debe mostrar "Acceso denegado". 
# Este tipo de programa se utiliza en muchos sitios web y sistemas para controlar el acceso. 
USUARIO_BBDD = "admin"
PASSWORD_BBDD = 1234
print("escribe un nombre para tu usuario")
usuario = input()
print("es necesario que te inventes una contraseña")
contraseña = int(input())
if(usuario == USUARIO_BBDD) and (contraseña == PASSWORD_BBDD): 
    print("acceso concedido")
else: 
    print("acceso denegado")