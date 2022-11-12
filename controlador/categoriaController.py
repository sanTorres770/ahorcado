import persistencia.tabla as persistencia
import modelo.categoriaModel as categoriaModel
import random as random
from random import shuffle

def elegirPalabraRandom(opcionElegida):

    listaDePalabras = categoriaModel.obtenerListaSegunCategoria(opcionElegida)
    shuffle(listaDePalabras)
    indiceRandom = random.randint(0,len(listaDePalabras)-1)

    return listaDePalabras[indiceRandom]