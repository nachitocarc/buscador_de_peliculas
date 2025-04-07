import json

class Actor:
    def __init__(self, nombre):
        self.__nombre = nombre

    def obtener_nombre(self):
        return self.__nombre

    def __str__(self):
        return self.__nombre

class Pelicula:
    def __init__(self, titulo, sinopsis, actores, poster, puntuacion, genero):
        self.__titulo = titulo
        self.__sinopsis = sinopsis
        self.__actores = actores
        self.__poster = poster
        self.__puntuacion = puntuacion
        self.__genero = genero

    def obtener_datos(self):
        return {
            "titulo": self.__titulo,
            "sinopsis": self.__sinopsis,
            "actores": [actor.obtener_nombre() for actor in self.__actores],
            "poster": self.__poster,
            "puntuacion": self.__puntuacion,
            "genero": self.__genero
        }

    def obtener_titulo(self):
        return self.__titulo

    def tiene_actor(self, actor):
        return actor.lower() in (actor.obtener_nombre().lower() for actor in self.__actores)

class Catalogo:
    def __init__(self, peliculas_json):
        self.__peliculas = self.__cargar_peliculas(peliculas_json)

    def __cargar_peliculas(self, archivo_json):
        with open(archivo_json, 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)
            return [
                Pelicula(
                    pelicula["titulo"],
                    pelicula["sinopsis"],
                    [Actor(nombre) for nombre in pelicula["actores"]],
                    pelicula["poster"],
                    pelicula["puntuacion"],
                    pelicula["genero"]
                )
                for pelicula in datos
            ]

    def obtener_generos(self):
        return list({pelicula.obtener_datos()["genero"] for pelicula in self.__peliculas})

    def obtener_titulos(self):
        return [pelicula.obtener_titulo() for pelicula in self.__peliculas]

    def buscar_pelicula(self, nombre):
        return [pelicula.obtener_datos() for pelicula in self.__peliculas if nombre.lower() in pelicula.obtener_titulo().lower()]

    def obtener_informacion_pelicula(self, titulo):
        for pelicula in self.__peliculas:
            if pelicula.obtener_titulo() == titulo:
                return pelicula.obtener_datos()

    def buscar_por_genero(self, genero):
        return [pelicula.obtener_datos() for pelicula in self.__peliculas if pelicula.obtener_datos()["genero"].lower() == genero.lower()]

    def obtener_actores(self):
        actores = set()
        for pelicula in self.__peliculas:
            actores.update(pelicula.obtener_datos()["actores"])
        return [Actor(nombre) for nombre in actores]

    def buscar_por_dos_actores(self, actor1, actor2):
        actor1, actor2 = actor1.lower(), actor2.lower()
        return [pelicula.obtener_datos() for pelicula in self.__peliculas
                if pelicula.tiene_actor(actor1) and pelicula.tiene_actor(actor2)]
