import platform
from os import system

CLASIFICACION = {
    0: 'Infrapeso: Delgadez severa',
    16: 'Infrapeso: Delgadez moderada',
    17: 'Infrapeso: Delgadez aceptable',
    18.5: 'Peso Normal',
    25: 'Sobrepeso',
    30: 'Obeso: Tipo I',
    35: 'Obeso: Tipo II',
    40: 'Obeso: Tipo III'
}

def _buscar_clave(diccionario, clave):
    claves_validas = [k for k in diccionario if k <= clave]
    if not claves_validas:
        return None
    mejor_clave = max(claves_validas)
    return diccionario[mejor_clave]


def bienvenida()->None:
    sys_name = platform.system()
    if sys_name == 'Windows':
        system('cls')
    else:
        system('clear')
    
    print('Bienvenido a su calculadora de IMC')
    print('-' * 46)
    print('')

def ingreso_de_datos()-> tuple[float, float]:
    while True:
        valor = input('Ingrese su peso (en Kg): ')
        try:
            peso = float(valor)
            break
        except ValueError:
            print('Debe ingresar un número válido')

    while True:
        valor = input('Ingrese su altura (en metros): ')
        try:
            altura = float(valor)
            break
        except ValueError:
            print('Debe ingresar un número válido')

    return peso, altura


bienvenida()
peso, altura = ingreso_de_datos()

imc = round(peso / (altura ** 2), 2)
clasif = _buscar_clave(CLASIFICACION, imc)
mensaje = f'\nEl IMC es: {imc} - ' + clasif
print(mensaje)
