import random

def videojuego():
    print('Bienvenido, adivina el numero aleatorio, mientras menos puntaje tengas mejor')
    puntaje = 0
    objetivo = random.randint(0,100)
    numero = int(input('Por favor ingrese un numero: '))
    while numero:
        puntaje+=1
        if numero > objetivo:
            numero = int(input('Elige un numero mas chico: '))
        elif numero < objetivo:
            numero = int(input('Elige un numero mas grande: '))
        else:
            print ('GANASTE!!')
            print ('Tu puntaje es: ' + str(puntaje))
            break


if __name__ == '__main__':
    videojuego()