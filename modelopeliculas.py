import json

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
            "actores": self.__actores,
            "poster": self.__poster,
            "puntuacion": self.__puntuacion,
            "genero": self.__genero
        }

    def tiene_actor(self, actor):
        return actor.lower() in (a.lower() for a in self.__actores)

    def obtener_titulo(self):
        return self.__titulo


class ModeloPeliculas:
    def __init__(self, peliculas_json):
        self.__peliculas = self.__cargar_peliculas(peliculas_json)

    def __cargar_peliculas(self, archivo_json):
        with open(archivo_json, 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)
            return [Pelicula(**pelicula) for pelicula in datos]

    def buscar_pelicula(self, nombre):
        nombre = nombre.lower()
        return [pelicula.obtener_datos() for pelicula in self.__peliculas if nombre in pelicula.obtener_titulo().lower()]

    def obtener_informacion_pelicula(self, titulo):
        for pelicula in self.__peliculas:
            if pelicula.obtener_titulo() == titulo:
                return pelicula.obtener_datos()

    def buscar_por_dos_actores(self, actor1, actor2):
        actor1 = actor1.lower()
        actor2 = actor2.lower()
        return [pelicula.obtener_titulo() for pelicula in self.__peliculas
                if pelicula.tiene_actor(actor1) and pelicula.tiene_actor(actor2)]

    def obtener_titulos(self):
        return [pelicula.obtener_titulo() for pelicula in self.__peliculas]

    def obtener_actores(self):
        actores = set()
        for pelicula in self.__peliculas:
            actores.update(pelicula.obtener_datos()["actores"])
        return list(actores)

