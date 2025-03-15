from vista_peliculas import BuscadorDePeliculas, DetallesPelicula
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QCompleter, QDialog, QVBoxLayout, QLabel


class Controlador:
    def __init__(self, modelo):
        self.__modelo = modelo
        self.vista = BuscadorDePeliculas(modelo, self)
        self.__cargar_peliculas()
        self.__configurar_completer(self.__modelo.obtener_titulos(), self.vista.line_edit)

        self.vista.generos.currentTextChanged.connect(self.__buscar_por_genero)
        self.vista.boton_buscar_pelicula.clicked.connect(self.__buscar_pelicula)
        self.vista.catalogo.itemClicked.connect(self.__mostrar_detalles_pelicula)

    def mostrar_ventana(self):
        self.vista.show()

    def __cargar_peliculas(self):
        self.vista.catalogo.clear()
        peliculas = self.__modelo.obtener_titulos()
        self.vista.catalogo.addItems(peliculas)

    def __buscar_pelicula(self):
        nombre = self.vista.line_edit.text().strip()
        if not nombre:
            self.__cargar_peliculas()
            return
        peliculas_encontradas = self.__modelo.buscar_pelicula(nombre)
        self.vista.catalogo.clear()
        self.vista.catalogo.addItems([p["titulo"] for p in peliculas_encontradas])

    def __mostrar_detalles_pelicula(self, item):
        titulo_pelicula = item.text()
        datos_pelicula = self.__modelo.obtener_informacion_pelicula(titulo_pelicula)

        if datos_pelicula:
            detalles_dialog = DetallesPelicula(
                datos_pelicula["titulo"],
                datos_pelicula["sinopsis"],
                datos_pelicula["puntuacion"],
                datos_pelicula["actores"],
                datos_pelicula["genero"],
                datos_pelicula["poster"],
                self.vista
            )
            detalles_dialog.exec()

    def __configurar_completer(self, opciones, line_edit):
        completer = QCompleter(opciones, self.vista)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        line_edit.setCompleter(completer)

    def __buscar_por_genero(self):
        genero = self.vista.generos.currentText().strip()
        peliculas_encontradas = self.__modelo.buscar_por_genero(genero)
        self.vista.catalogo.clear()
        self.vista.catalogo.addItems([p["titulo"] for p in peliculas_encontradas])

    def buscar_por_dos_actores(self, actor1, actor2):
        if not actor1.strip() or not actor2.strip():
            error = QDialog(self.vista)
            error.setWindowTitle("Error")
            layout = QVBoxLayout(error)
            error_label = QLabel("ingrese el nombre de los 2 actores.", error)
            layout.addWidget(error_label)
            error.setLayout(layout)
            error.exec()
            return

        peliculas_encontradas = self.__modelo.buscar_por_dos_actores(actor1, actor2)
        if peliculas_encontradas:
            self.vista.actualizar_catalogo(peliculas_encontradas)
        else:
            self.vista.actualizar_catalogo([])

