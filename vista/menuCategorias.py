import os
import time



def categorias():
    seleccion = 0
    opcionElegida = ""
    while seleccion <= 0 or seleccion > 4:
        os.system('cls')
        print('estas a punto de empezar el mejor juego de ahorcado del mundo')
        print('')
        print('Elige la categoria')
        print('-------------------------------------------------------------')
        print('|1| Lenguajes de programación|')
        print('-------------------------------------------------------------')
        print('|2| Animales|')
        print('-------------------------------------------------------------')
        print('|3| Temas de exposicion|')
        print('-------------------------------------------------------------')
        print('|4| Nombres|')
        print('-------------------------------------------------------------')
        seleccion = int(input('Ingresa el numero de la categoria: '))
        match seleccion:
            case 0:
                input(f"El {seleccion} no es una opción válida. Presione cualquier tecla para intentarlo de nuevo.")
                os.system('cls')
            case 1:
                os.system('cls')
                print('Preparando la palabra.')
                time.sleep(1)
                os.system('cls')
                print('Preparando la palabra..')
                time.sleep(1)
                os.system('cls')
                print('Preparando la palabra...')
                time.sleep(1)
                os.system('cls')
                print('El juego esta listo...')
                time.sleep(0.5)
                opcionElegida = "lenguajes"
                print(opcionElegida)
                input('')
                categorias()
            case 2:
                os.system('cls')
                print('Preparando la palabra.')
                time.sleep(1)
                os.system('cls')
                print('Preparando la palabra..')
                time.sleep(1)
                os.system('cls')
                print('Preparando la palabra...')
                time.sleep(1)
                os.system('cls')
                print('El juego esta listo...')
                time.sleep(0.5)
                opcionElegida = "animales"
                print(opcionElegida)
                input('')
                categorias()
            case 3:
                os.system('cls')
                print('Preparando la palabra.')
                time.sleep(1)
                os.system('cls')
                print('Preparando la palabra..')
                time.sleep(1)
                os.system('cls')
                print('Preparando la palabra...')
                time.sleep(1)
                os.system('cls')
                print('El juego esta listo...')
                time.sleep(0.5)
                opcionElegida = "temas"
                print(opcionElegida)
                input('')
                categorias()
            case 4:
                os.system('cls')
                print('Preparando la palabra.')
                time.sleep(1)
                os.system('cls')
                print('Preparando la palabra..')
                time.sleep(1)
                os.system('cls')
                print('Preparando la palabra...')
                time.sleep(1)
                os.system('cls')
                print('El juego esta listo...')
                time.sleep(0.5)
                opcionElegida = "nombres"
                print(opcionElegida)
                input('')
                categorias()

