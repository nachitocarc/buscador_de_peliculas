import json

class Pelicula:
    def __init__(self, titulo, sinopsis, actores, género, puntuacion, poster):
        self.titulo = titulo
        self.sinopsis = sinopsis
        self.actores = actores
        self.género = género
        self.puntuacion = puntuacion
        self.poster = poster


class ModeloPeliculas:
    def __init__(self, peliculas_json):
        self.__peliculas = self.__cargar_peliculas(peliculas_json)

    def __cargar_peliculas(self, archivo_json):
        with open(archivo_json, 'r', encoding='utf-8') as archivo:
            peliculas_data = json.load(archivo)
            return [Pelicula(**data) for data in peliculas_data]

    def buscar_pelicula(self, nombre):
        return [pelicula for pelicula in self.__peliculas if nombre.lower() in pelicula.titulo.lower()]

    def obtener_informacion_pelicula(self, titulo):
        for pelicula in self.__peliculas:
            if pelicula.titulo == titulo:
                return pelicula

    def buscar_por_dos_actores(self, actor1, actor2):
        actor1_lower = actor1.lower()
        actor2_lower = actor2.lower()
        return [pelicula.titulo for pelicula in self.__peliculas
                if actor1_lower in (a.lower() for a in pelicula.actores)
                and actor2_lower in (a.lower() for a in pelicula.actores)]

    def obtener_titulos(self):
        return [pelicula.titulo for pelicula in self.__peliculas]

    def obtener_actores(self):
        actores = set()
        for pelicula in self.__peliculas:
            actores.update(pelicula.actores)
        return list(actores)

    def obtener_peliculas(self):
        return self.__peliculas
