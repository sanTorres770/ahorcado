import persistencia.tablas as persistencia
import modelo.palabraModel as palabraModel
import random as random
from random import shuffle

def elegirPalabraRandom(opcionElegida):

    listaDePalabras = palabraModel.obtenerListaSegunCategoria(opcionElegida)
    shuffle(listaDePalabras)
    indiceRandom = random.randint(0,len(listaDePalabras)-1)

    return listaDePalabras[indiceRandom]