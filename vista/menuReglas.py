import time
import vista.entrada as entrada


def reglas():
    s= True
    while(s):
        print('*********** MENU DE LAS REGLAS ************')
        print('-------------------------------------------')
        print('1. Tendras 10 intentos\n'
              '2. El juego solo se acaba cuando ganes (encontraste la palabra)\n'
              '3. El juego solo se acaba cuando (gastes los 10 intentos))\n'
              '4. La palabra se dara al azar dependiendo la categoria escogida')
        input('Si ya terminaste de leer presiona ENTER para continuar')
        print('regresando al menu...', time.sleep(2))
        entrada.menuEntradas()
        s = False