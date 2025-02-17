import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QCompleter, QDialog, QVBoxLayout, QLabel, QPushButton, \
    QLineEdit
from modelopeliculas import ModeloPeliculas
from vistapeliculas import UiMainWindow, DetallesPeliculaDialog

class MainWindow(QMainWindow):
    def __init__(self, modelo):
        super().__init__()
        self.__ui = UiMainWindow()
        self.__ui.setup_ui(self)

        self.__modelo = modelo

        self.__cargar_peliculas()
        self.__configurar_completer(self.__modelo.obtener_titulos(), self.__ui.line_edit)

        self.__ui.boton_buscar_pelicula.clicked.connect(self.__buscar_pelicula)
        self.__ui.boton_buscar_por_actores.clicked.connect(self.__abrir_buscar_por_actores)
        self.__ui.catalogo.itemClicked.connect(self.__mostrar_detalles_pelicula)

    def __cargar_peliculas(self):
        self.__ui.catalogo.clear()
        peliculas = self.__modelo.obtener_titulos()
        self.__ui.catalogo.addItems(peliculas)

    def __buscar_pelicula(self):
        nombre = self.__ui.line_edit.text().strip()
        if not nombre:
            self.__cargar_peliculas()
            return
        peliculas_encontradas = self.__modelo.buscar_pelicula(nombre)
        self.__ui.catalogo.clear()
        self.__ui.catalogo.addItems([p["titulo"] for p in peliculas_encontradas])

    def __mostrar_detalles_pelicula(self, item):
        titulo_pelicula = item.text()
        datos_pelicula = self.__modelo.obtener_informacion_pelicula(titulo_pelicula)

        if datos_pelicula:
            detalles_dialog = DetallesPeliculaDialog(datos_pelicula, self)
            detalles_dialog.exec()

    def __configurar_completer(self, opciones, line_edit):
        completer = QCompleter(opciones, self)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        line_edit.setCompleter(completer)

    def __abrir_buscar_por_actores(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Buscar por Actores")
        layout = QVBoxLayout(dialog)

        label1 = QLabel("Ingresa el nombre del primer actor:", dialog)
        layout.addWidget(label1)
        actor1_input = QLineEdit(dialog)
        layout.addWidget(actor1_input)
        self.__configurar_completer(self.__modelo.obtener_actores(), actor1_input)

        label2 = QLabel("Ingresa el nombre del segundo actor:", dialog)
        layout.addWidget(label2)
        actor2_input = QLineEdit(dialog)
        layout.addWidget(actor2_input)
        self.__configurar_completer(self.__modelo.obtener_actores(), actor2_input)

        boton_buscar = QPushButton("Buscar", dialog)
        layout.addWidget(boton_buscar)

        boton_buscar.clicked.connect(lambda: self.__buscar_por_dos_actores(actor1_input.text(), actor2_input.text()))

        dialog.setLayout(layout)
        dialog.exec()

    def __buscar_por_dos_actores(self, actor1, actor2):
        if not actor1.strip() or not actor2.strip():
            error_dialog = QDialog(self)
            error_dialog.setWindowTitle("Error")
            layout = QVBoxLayout(error_dialog)
            error_label = QLabel("Ingresa el nombre de los 2 actores.", error_dialog)
            layout.addWidget(error_label)
            error_dialog.setLayout(layout)
            error_dialog.exec()
            return
        peliculas_encontradas = self.__modelo.buscar_por_dos_actores(actor1, actor2)

        self.__ui.catalogo.clear()
        for titulo in peliculas_encontradas:
            self.__ui.catalogo.addItem(titulo)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    modelo = ModeloPeliculas("peliculas.json")
    window = MainWindow(modelo)
    window.show()
    sys.exit(app.exec())
