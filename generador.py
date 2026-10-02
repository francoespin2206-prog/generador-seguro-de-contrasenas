import random 
print("generador de contraseñas seguras")
longitud= int(input("¿Cuantos caracteres?"))

if longitud < 8:
    print("La contraseña debe tener al menos 8 caracteres")
else:
    caracteres= "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-+"
    contraseña= ""
    print("Contraseña generada:", contraseña)

    for i in range(longitud):
        numero_aleatorio= random.randint(0, len(caracteres)-1)
        contraseña += caracteres[numero_aleatorio]
print("Contraseña final", contraseña)
