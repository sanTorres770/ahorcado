import os
import time
import vista.menuPrincipal as menuPrincipal
from tabulate import tabulate
import controlador.categoriaController as categoriaContoller


def categorias():
    seleccion = 0
    tablaCategorias = categoriaContoller.obtenerListaDeCategorias()

    while seleccion <= 0 or seleccion > 4:
        os.system('cls')
        print('Estás a punto de empezar el mejor juego de ahorcado!')
        print('')
        print('Elige la categoria:')
        print("")
        print(tabulate(tablaCategorias, tablefmt="pretty"))
        print("")

        try:
            seleccion = int(input('Ingresa la opción deseada => '))
            match seleccion:
                case 0:
                    input(f"El {seleccion} no es una opción válida. Presione ENTER tecla para intentarlo de nuevo.")
                    os.system('cls')
                case 1:
                    os.system('cls')
                    print('Preparando la palabra.')
                    time.sleep(0.7)
                    os.system('cls')
                    print('Preparando la palabra..')
                    time.sleep(0.7)
                    os.system('cls')
                    print('Preparando la palabra...')
                    time.sleep(0.7)
                    os.system('cls')
                    print('El juego está listo...')
                    time.sleep(0.5)
                    opcionElegida = "lenguajes"
                    menuPrincipal.juego(opcionElegida,tablaCategorias[0][1])
                case 2:
                    os.system('cls')
                    print('Preparando la palabra.')
                    time.sleep(0.7)
                    os.system('cls')
                    print('Preparando la palabra..')
                    time.sleep(0.7)
                    os.system('cls')
                    print('Preparando la palabra...')
                    time.sleep(0.7)
                    os.system('cls')
                    print('El juego está listo...')
                    time.sleep(0.5)
                    opcionElegida = "animales"
                    menuPrincipal.juego(opcionElegida,tablaCategorias[1][1])
                case 3:
                    os.system('cls')
                    print('Preparando la palabra.')
                    time.sleep(0.7)
                    os.system('cls')
                    print('Preparando la palabra..')
                    time.sleep(0.7)
                    os.system('cls')
                    print('Preparando la palabra...')
                    time.sleep(0.7)
                    os.system('cls')
                    print('El juego está listo...')
                    time.sleep(0.5)
                    opcionElegida = "temas"
                    menuPrincipal.juego(opcionElegida,tablaCategorias[2][1])
                case 4:
                    os.system('cls')
                    print('Preparando la palabra.')
                    time.sleep(0.7)
                    os.system('cls')
                    print('Preparando la palabra..')
                    time.sleep(0.7)
                    os.system('cls')
                    print('Preparando la palabra...')
                    time.sleep(0.7)
                    os.system('cls')
                    print('El juego está listo...')
                    time.sleep(0.5)
                    opcionElegida = "nombres"
                    menuPrincipal.juego(opcionElegida,tablaCategorias[3][1])
                case 5:
                    os.system('cls')
                    print('Preparando la palabra.')
                    time.sleep(0.7)
                    os.system('cls')
                    print('Preparando la palabra..')
                    time.sleep(0.7)
                    os.system('cls')
                    print('Preparando la palabra...')
                    time.sleep(0.7)
                    os.system('cls')
                    print('El juego está listo...')
                    time.sleep(0.5)
                    opcionElegida = "paises"
                    menuPrincipal.juego(opcionElegida,tablaCategorias[4][1])
        except ValueError:
            input(f"Ingresó una opción no válida. Presione cualquier tecla para intentarlo de nuevo.")
