import random 
print("generador de contraseñas seguras") #Título del programa
longitud= int(input("¿Cuantos caracteres?")) #Pedir al usuario la longitud de la contraseña

if longitud < 8: #si tiene menos de 8 caracteres, va a salir un error ya que el minimo es 8 caracteres
    print("La contraseña debe tener al menos 8 caracteres")
else: #si cumple con 8 caracteres o más va a empezar a generar la contraseña
    caracteres= "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-+" #letras en mayusuclas y minusuclas ,simbolos lascuales se van a utilizar para generar la contraseña
    contraseña= ""

    for i in range(longitud): #repite el proceso de generar un caracter aleatorio hasta que se cumpla la longitud de la contraseña
        numero_aleatorio= random.randint(0, len(caracteres)-1)
        contraseña += caracteres[numero_aleatorio]
    print("Contraseña final", contraseña) #contraseña final generada

