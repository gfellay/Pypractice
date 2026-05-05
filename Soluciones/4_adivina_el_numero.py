import random
from os import system
import platform

def bienvenida()->None:
    sys_name = platform.system()
    if sys_name == 'Windows':
        system('cls')
    else:
        system('clear')
    
    print('Bienvenido al juego para averiguar el número')
    print('-' * 46)
    print('El juego consiste en averiguar un número entre 1 y 100')
    print('En cada iteración se le pedirá que ingrese un valor hasta que acierte')
    print('En caso que quiera finalizar el juego antes, presione 0 (cero)')
    print('\nEmpecemos...\n')


def generar_numero()->int:
    random.seed()
    valor = int(random.random() * 100 + 1)
    return valor


def preguntar_al_usuario()->int:
    while True:
        valor = input('Ingrese un valor entre 1 y 100 o 0 (cero) para finalizar: ')
        if valor.isdigit():
            numero = int(valor)
            if 0 <= numero <= 100:
                return numero
            else:
                print('El número está fuera del rango válido')
        else:
            print('Debe ingresar un número')


def evaluar_resultado(valor: int, ingresado: int, intento: int)->bool:
    if ingresado == valor:
        print(f'Felicitaciones! Encontró el número {valor}, luego de {intento} intentos!')
        return False

    dif = valor - ingresado        
    if dif > 50:
        msj = 'Demasiado bajo.'
    elif dif > 20:
        msj = 'El número es bajo.'
    elif dif > 5:
        msj = 'El número es un poco bajo.'
    elif dif < -50:
        msj = 'Demasiado alto.'
    elif dif < -20:
        msj = 'El número es alto.'
    elif dif < -5:
        msj = 'El número es un poco alto.'
    else:
        msj = 'Cerca'

    mensaje = f'Intento {intento}. Número ingresado: {ingresado}. {msj}'
    print(mensaje)
    return True

bienvenida()
valor = generar_numero()
#print(valor)
centinela = True
it = 1
while centinela:
    ingresado = preguntar_al_usuario()
    if ingresado == 0:
        centinela = False
        break
    centinela = evaluar_resultado(valor=valor, ingresado=ingresado, intento=it)
    it +=1

print('Gracias por usar la app!\nEspero el juego le haya gustado')