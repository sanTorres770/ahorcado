import time
import os
import persistencia.tablas as persistencia
import controlador.palabraController as palabraController
import vista.entrada as entrada
import vista.fin as fin


def juego(opcionElegida, categoria):
    aciertos = 0
    intentos = 0
    fallos = 0
    letrasCorrectas = ""
    figuraAhorcado = persistencia.AHORCADO
    tuplaPalabra = palabraController.elegirPalabraRandom(opcionElegida)
    palabraADescubrir = tuplaPalabra[0]
    palabraADescubrirLista = list(palabraADescubrir)
    lineasPalabra = crearLineas(palabraADescubrir)

    while aciertos <= tuplaPalabra[1]:
        os.system("cls")

        if fallos == 1:
            veces = "vez"
        else:
            veces = "veces"

        print(f"        Categoría: {categoria}      Has Fallado {fallos} {veces}")
        print('\t' * 7, figuraAhorcado[fallos])
        print("")
        mostrarLineas(lineasPalabra)
        print("")
        letraIngresada = input("Ingresa una letra =>").lower()

        if letraIngresada not in letrasCorrectas:

            vecesQueSeRepite = palabraADescubrirLista.count(letraIngresada)

            if vecesQueSeRepite == 0:
                print("")
                print('\t'*1,f"    Fallaste! La letra '{letraIngresada.upper()}' no está en la palabra escondida.")
                input("                 Presiona ENTER para intentarlo de nuevo...")
                fallos += 1

            if vecesQueSeRepite == 1:

                indiceLetraAdivinada = palabraADescubrir.index(letraIngresada)
                lineasPalabra[indiceLetraAdivinada] = letraIngresada
                aciertos += 1
                intentos += 1
                letrasCorrectas = letrasCorrectas + letraIngresada

            else:

                for i in range(len(palabraADescubrir)):
                    if palabraADescubrirLista[i] == letraIngresada:
                        lineasPalabra[i] = letraIngresada
                        aciertos += 1
                        intentos += 1
                        letrasCorrectas = letrasCorrectas + letraIngresada

            if fallos == 10:
                os.system("cls")
                print(figuraAhorcado[fallos])
                print("")
                print('\t' * 3, "Has perdido :(")
                print('\t' * 2, f"La palabra escondida era '{palabraADescubrir.upper()}'")
                print()
                input("Presiona ENTER para Continuar ...")
                finalDelJuego()
                break

            if aciertos == tuplaPalabra[1]:
                os.system("cls")
                print(figuraAhorcado[fallos])
                print("")
                mostrarLineas(lineasPalabra)
                print("")
                print('\t' * 2, "  Adivinaste la palabra... Bien hecho!")
                print("")
                input("Presiona ENTER para Continuar ...")
                finalDelJuego()
                break
        else:

            if letraIngresada != "":
                print("")
                print('\t'*3,f"La letra '{letraIngresada.upper()}' ya se descubrió.")
                input("                 Presiona ENTER para intentarlo de nuevo...")

def crearLineas(palabra):
    lineas = []

    for letras in palabra:

        if letras == " ":
            lineas.append(" ")
        else:
            lineas.append("__")

    return lineas


def mostrarLineas(listaDeLineas):
    lineas = ""

    for letras in listaDeLineas:
        lineas = lineas + " " + letras.upper()

    if len(listaDeLineas) >= 2 and len(listaDeLineas) <= 4:
        print('\t' * 4, lineas)
    if len(listaDeLineas) > 4 and len(listaDeLineas) <= 6:
        print('\t' * 3, lineas)
    if len(listaDeLineas) > 6 and len(listaDeLineas) <= 10:
        print('\t' * 3, lineas)
    if len(listaDeLineas) > 10:
        print('\t' * 2, lineas)


def finalDelJuego():
    opcion = " "

    while opcion != "N" and opcion != "S":
        os.system("cls")

        print()
        print()
        print('\t' * 3, "*** ¿deseas jugar de nuevo? ***")
        print('\t' * 3, "")
        print('\t' * 2, "Si la respuesta es SI, presiona la letra S")
        print('\t' * 2, "Si la respuesta es NO, presiona la letra N")
        opcion = input("==>").upper()

    if opcion == "S":
        entrada.menuEntradas()
    else:
        fin.finalizar()
