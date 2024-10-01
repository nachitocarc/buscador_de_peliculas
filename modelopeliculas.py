class ModeloPeliculas:
    def __init__(self):
        self._peliculas = [
            {
                'titulo': "Son como niños",
                'sinopsis': "Un grupo de amigos se reúne para revivir su infancia.",
                'actores': ["Adam Sandler", "Kevin James"],
                'puntuacion': "6.0"
            },
            {
                'titulo': "Titanic",
                'sinopsis': "Historia de amor en el famoso transatlántico.",
                'actores': ["Leonardo DiCaprio", "Kate Winslet"],
                'puntuacion': "7.8"
            },
            {
                'titulo': "Mi primer beso",
                'sinopsis': "La historia de un primer amor adolescente.",
                'actores': ["Anna Chlumsky", "Macaulay Culkin"],
                'puntuacion': "6.8"
            },
            {
                'titulo': "Chiquito pero peligroso",
                'sinopsis': "Un niño es el único que puede salvar el día.",
                'actores': ["Kevin Spacey", "Drew Barrymore"],
                'puntuacion': "5.6"
            },
            {
                'titulo': "Violet y Finch",
                'sinopsis': "Dos adolescentes se encuentran en un viaje emocional.",
                'actores': ["Justice Smith", "Elle Fanning"],
                'puntuacion': "6.5"
            },
            {
                'titulo': "El hijo de la novia",
                'sinopsis': "Un hombre intenta reconciliarse con su madre.",
                'actores': ["Ricardo Darín", "Natalia Verbeke"],
                'puntuacion': "7.4"
            },
            {
                'titulo': "Super cool",
                'sinopsis': "Tres amigos viven una loca noche.",
                'actores': ["Jonah Hill", "Michael Cera"],
                'puntuacion': "7.0"
            },
            {
                'titulo': "Un espía y medio",
                'sinopsis': "Un contador se convierte en un espía.",
                'actores': ["Dwayne Johnson", "Kevin Hart"],
                'puntuacion': "6.2"
            },
            {
                'titulo': "Entre la vida y la muerte",
                'sinopsis': "Un hombre lucha por sobrevivir tras un accidente.",
                'actores': ["Benicio Del Toro", "Jason Patric"],
                'puntuacion': "6.1"
            }
        ]

    def buscar_pelicula(self, nombre):
        return [pelicula for pelicula in self._peliculas if nombre.lower() in pelicula['titulo'].lower()]

    def obtener_informacion_pelicula(self, titulo):
        for pelicula in self._peliculas:
            if pelicula['titulo'] == titulo:
                return pelicula

    def buscar_por_actor(self, actor):
        return [pelicula['titulo'] for pelicula in self._peliculas if actor in pelicula['actores']]
