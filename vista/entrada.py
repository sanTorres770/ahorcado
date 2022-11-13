import os
import time
import vista.menuReglas as menuReglas
import vista.menuCategorias as menuCategorias
import vista.fin as fin
import tabulate


def menuEntradas():
    seleccion = 0
    while seleccion <= 0 or seleccion > 3:
        os.system('cls')
        print('\t' * 2, '******* BIENVENIDO AL AHORCADO REMINGTON *******')
        print('\t' * 4, '______________')
        print('\t' * 4, '    |        |')
        print('\t' * 4, '    O        |')
        print('\t' * 4, '   /|\       |')
        print('\t' * 4, '   / \       |')
        print('\t' * 4, '  /   \      |')
        print('\t' * 1, '------------------------------------------------------------')
        print('\t' * 1, '| Ahorcado, el juego donde tienes que adivinar la palabra  |')
        print('\t' * 1, '|                       escondida.                         |')
        print('\t' * 1, '------------------------------------------------------------')
        print('\t' * 1, '------------------------------------------------------------')
        print('\t' * 1, '******************** OPCIONES DEL JUEGO ********************')
        print('\t' * 1, '|                        1.Jugar                           |')
        print('\t' * 1, '|                      2.Ver reglas                        |')
        print('\t' * 1, '|                    3.Salir del juego                     |')
        print('\t' * 1, '------------------------------------------------------------')

        try:
            seleccion = int(input('Ingresa la opción deseada: '))

            match seleccion:
                case 0:
                    input(f"El {seleccion} no es una opción válida. Presione cualquier tecla para intentarlo de nuevo.")
                case 1:
                    print("\t" * 3, "Entrando al juego...")
                    time.sleep(0.75)
                    menuCategorias.categorias()
                case 2:
                    print("\t" * 3, "Entrando a las reglas...")
                    time.sleep(0.75)
                    menuReglas.reglas()
                case 3:
                    print("                        ¿desea salir del AHORCADO?")
                    print()
                    print("SI ==> ENTER")
                    print("NO ==> X")
                    op = input().upper()
                    os.system("cls")

                    if op == "":
                        fin.finalizar()
                    elif op == "X":
                        menuEntradas()
                case _:
                    input(f"El {seleccion} no es una opción válida. Presione cualquier tecla para intentarlo de nuevo.")

        except ValueError:
            input(f"Ingresó una opción no válida. Presione cualquier tecla para intentarlo de nuevo.")
