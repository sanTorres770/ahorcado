import time
import vista.entrada as entrada
import os


def reglas():
    os.system("cls")
    opcion = True
    while opcion:
        print('\t'*2,'*********** REGLAS DEL JUEGO ************')
        print('\t'*2,'-----------------------------------------')
        print('1. Debes adivinar la palabra escondida, ingresando las letras una por una.')
        print('2. Cuando descubras todas las letras, habrás ganado.')
        print('3. Si llegas a los 10 fallos perderás y el juego terminará.')
        print('4. La palabra se dará al azar dependiendo de la categoria escogida')
        print("")
        input('    ****   Si ya terminaste de leer presiona ENTER para continuar   ****')
        print('Regresando al menú...')
        time.sleep(0.5)
        entrada.menuEntradas()
        opcion = False
