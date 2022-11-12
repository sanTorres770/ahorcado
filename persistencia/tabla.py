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

categorias = {"animales": [Palabra("perro", 5), Palabra("gato", 4), Palabra("araña",5)],
              "lenguajes": [Palabra("python", 6), Palabra("java", 4), Palabra("javascript",10)],
              "temas": [Palabra("grafos", 6), Palabra("pilas", 5)],
              "nombres": [Palabra("camilo", 6), Palabra("santiago", 8)]
              }
