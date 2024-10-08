#modelo
import json


class ModeloPeliculas:
    def __init__(self, peliculas_json):
        self._peliculas = self._cargar_peliculas(peliculas_json)

    def _cargar_peliculas(self, archivo_json):
        with open(archivo_json, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)

    def buscar_pelicula(self, nombre):
        return [pelicula for pelicula in self._peliculas if nombre.lower() in pelicula['titulo'].lower()]

    def obtener_informacion_pelicula(self, titulo):
        for pelicula in self._peliculas:
            if pelicula['titulo'] == titulo:
                return pelicula

    def buscar_por_actor(self, actor):
        return [pelicula['titulo'] for pelicula in self._peliculas if actor in pelicula['actores']]
