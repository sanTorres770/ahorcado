import persistencia.tablas as persistencia


def obtenerListaSegunCategoria(opcionElegida):

    return persistencia.tablaPalabras[opcionElegida]
