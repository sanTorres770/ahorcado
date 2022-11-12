import time
import os
import persistencia.tabla as persistencia
import controlador.categoriaController as categoriaController


def juego(opcionElegida):
    aciertos = 0
    intentos = 0
    fallos = 0
    figuraAhorcado = persistencia.AHORCADO
    tuplaPalabra = categoriaController.elegirPalabraRandom(opcionElegida)
    palabraADescubrir = tuplaPalabra[0]
    palabraADescubrirLista = list(palabraADescubrir)
    lineasPalabra = crearLineas(palabraADescubrir)


    while aciertos <= len(palabraADescubrir):
        os.system("cls")
        print(figuraAhorcado[fallos])
        print("")
        mostrarLineas(lineasPalabra)

        letraIngresada = input("ingrese la letra ").lower()

        vecesQueSeRepite = palabraADescubrirLista.count(letraIngresada)

        if vecesQueSeRepite == 0:
            print(f"La letra {letraIngresada} no está en la palabra escondida.")
            fallos += 1

        if vecesQueSeRepite == 1:

            indiceLetraAdivinada = palabraADescubrir.index(letraIngresada)
            lineasPalabra[indiceLetraAdivinada] = letraIngresada
            aciertos += 1
            intentos += 1

        else:

            for i in range(len(palabraADescubrir)):
                if palabraADescubrirLista[i] == letraIngresada:
                    lineasPalabra[i] = letraIngresada
                    aciertos += 1
                    intentos += 1

        if fallos == 7:
            print(figuraAhorcado[fallos-1])
            print("perdió")
            break

        if aciertos == len(palabraADescubrir):
            print(figuraAhorcado[fallos])
            print("")
            mostrarLineas(lineasPalabra)
            print("Ganó")
            break


def crearLineas(palabra):
    lineas = []

    for letras in palabra:
        lineas.append("__")

    return lineas


def mostrarLineas(listaDeLineas):
    lineas = ""

    for letras in listaDeLineas:
        lineas = lineas + " " + letras

    print(lineas)
