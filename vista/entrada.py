import os
import time
import vista.menuReglas as menuReglas
import vista.menuCategorias as menuCategorias
import vista.fin as fin
import tabulate


def menuEntradas():

    seleccion = 0
    while seleccion <= 0 or seleccion > 3 :
        os.system('cls')
        print('************ BIENVENIDO AL AHORACDO REMINGTON **************')
        print('______________\n'
            '    |        |\n'
            '    O        |\n'
            '   /|\       |\n'
            '  / | \      |\n'
            '    |        |\n'
            '   / \       |\n'
            '  /   \      |\n')
        print('------------------------------------------------------------')
        print('| Ahorcado, el juego donde tienes que adivinar la palabra  |\n'
              '|                       escondida.                         |')
        print('------------------------------------------------------------')
        print('------------------------------------------------------------')
        print('******************** OPCIONES DEL JUEGO ********************')
        print('|                        1.Entrar                          |')
        print('|                      2.Ver reglas                        |')
        print('|                    3.Salir del juego                     |')
        print('------------------------------------------------------------')

        try:
            seleccion = int(input ('Ingresa el numero para ingresar al menu: '))
            match seleccion:
                case 0:
                    input(f"El {seleccion} no es una opción válida. Presione cualquier tecla para intentarlo de nuevo.")
                case 1:
                    print("\t" * 3, "Llendo a la entrada del juego...")
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
