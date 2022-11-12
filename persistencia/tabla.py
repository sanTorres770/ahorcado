import clases.categoria as categoria

AHORCADO = ['''
          +---+
          |   |
              |
              |
              |
              |
        =========''', '''
          +---+
          |   |
          O   |
              |
              |
              |
        =========''', '''
          +---+
          |   |
          O   |
          |   |
              |
              |
        =========''', '''
          +---+
          |   |
          O   |
         /|   |
              |
              |
        =========''', '''
          +---+
          |   |
          O   |
         /|\  |
              |
              |
        =========''', '''
          +---+
          |   |
          O   |
         /|\  |
         /    |
              |
        =========''', '''
          +---+
          |   |
          O   |
         /|\  |
         / \  |
              |
        =========''','''
          +---+
          |   |
          O   |
         /|\  |
          |   |
         / \  |
              |
        =========''','''
          +---+
          |   |
          O   |
         /|\  |
          |   |
         / \  |
        /   \ |
        =========''','''
          +---+
          |   |
         (O)  |
         /|\  |
          |   |
         / \  |
        /   \ |
        =========''','''
          +---+
          |   |
          x   |
         /|\  |
          |   |
         / \  |
        /   \ |
        =========''']

Palabra = categoria.Palabra

categorias = {"animales": [Palabra("perro", 5), Palabra("gato", 4), Palabra("araña",5), Palabra("leon",4), Palabra("jirafa",6), Palabra("hipopotamo",10), Palabra("cebra",5), Palabra("pato",4), Palabra("jaguar",6), Palabra("leopardo",8)],
              "lenguajes": [Palabra("python", 6), Palabra("java", 4), Palabra("javascript",10), Palabra("c++",3), Palabra("php",3), Palabra("sql",3), Palabra("c#",2), Palabra("ruby",4), Palabra("go",2), Palabra("perl",4)],
              "temas": [Palabra("grafos en java", 12), Palabra("grafos en python",14), Palabra("arboles en python",15), Palabra("arboles en java",13), Palabra("pilas y colas en java",17), Palabra("pilas y colas en python",19)],
              "nombres": [Palabra("camilo", 6), Palabra("santiago", 8), Palabra("federico",8), Palabra("katherine",9), Palabra("miler",5), Palabra("mauricio",8), Palabra("erika",5), Palabra("julian",6), Palabra("manuel",6), Palabra("miguel",6)],
              "paises": [Palabra("colombia",8), Palabra("venezuela",9), Palabra("peru",4), Palabra("ecuador",7), Palabra("chile",5), Palabra("argentina",9), Palabra("uruguay",8), Palabra("brasil",6), Palabra("paraguay",8), Palabra("bolivia",7)]
              }
