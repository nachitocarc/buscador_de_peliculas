from PySide6.QtCore import QMetaObject, Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (QGridLayout, QLabel, QLineEdit, QPushButton, QWidget, QListWidget, QDialog, QVBoxLayout, QComboBox, QMainWindow, QCompleter)

class BuscadorDePeliculas(QMainWindow):
    def __init__(self, modelo, controlador):
        super().__init__()
        self.__modelo = modelo
        self.controlador = controlador
        self.__configurar_ui()


    def __configurar_ui(self):
        self.setObjectName("Buscador de peliculas")
        self.resize(800, 600)
        self.centralwidget = QWidget(self)
        self.gridLayout = QGridLayout(self.centralwidget)

        self.boton_buscar_pelicula = QPushButton("Buscar", self.centralwidget)
        self.gridLayout.addWidget(self.boton_buscar_pelicula, 0, 3, 1, 1)

        self.line_edit = QLineEdit(self.centralwidget)
        self.line_edit.setPlaceholderText("Introduzca el nombre de la película")
        self.gridLayout.addWidget(self.line_edit, 0, 2, 1, 1)

        self.boton_buscar_por_actores = QPushButton("Buscar por actores", self.centralwidget)
        self.gridLayout.addWidget(self.boton_buscar_por_actores, 0, 0, 1, 1)

        self.label = QLabel("Película:", self.centralwidget)
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.catalogo = QListWidget(self.centralwidget)
        self.gridLayout.addWidget(self.catalogo, 2, 0, 1, 4)

        self.generos = QComboBox(self.centralwidget)
        self.gridLayout.addWidget(self.generos, 0, 1, 1, 1)
        self.generos.addItems(self.__modelo.obtener_generos())

        self.setCentralWidget(self.centralwidget)
        QMetaObject.connectSlotsByName(self)

        self.boton_buscar_por_actores.clicked.connect(self.__abrir_buscar_por_actores)

    def __abrir_buscar_por_actores(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Buscar por Actores")
        layout = QVBoxLayout(dialog)

        label1 = QLabel("Ingresa el nombre del primer actor:", dialog)
        layout.addWidget(label1)
        actor1_input = QLineEdit(dialog)
        layout.addWidget(actor1_input)

        label2 = QLabel("Ingresa el nombre del segundo actor:", dialog)
        layout.addWidget(label2)
        actor2_input = QLineEdit(dialog)
        layout.addWidget(actor2_input)

        actores = [actor.obtener_nombre() for actor in self.__modelo.obtener_actores()]
        self.__configurar_completer(actores, actor1_input)
        self.__configurar_completer(actores, actor2_input)

        boton_buscar = QPushButton("Buscar", dialog)
        layout.addWidget(boton_buscar)

        boton_buscar.clicked.connect(
            lambda: self.controlador.buscar_por_dos_actores(actor1_input.text(), actor2_input.text()))
        dialog.setLayout(layout)
        dialog.exec()

    def actualizar_catalogo(self, peliculas):
        self.catalogo.clear()
        for pelicula in peliculas:
            self.catalogo.addItem(pelicula["titulo"])

    def __configurar_completer(self, opciones, line_edit):
        completer = QCompleter(opciones, self)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        line_edit.setCompleter(completer)


class DetallesPelicula(QDialog):
    def __init__(self, titulo, sinopsis, puntuacion, actores, genero, poster, parent=None):
        super().__init__(parent)
        self.setWindowTitle(titulo)

        layout = QVBoxLayout(self)

        poster_label = QLabel(self)
        poster_pixmap = QPixmap(poster)

        if poster_pixmap.isNull():
            poster_label.setText("No se pudo cargar el póster.")
        else:
            poster_label.setPixmap(poster_pixmap.scaled(200, 300))

        layout.addWidget(poster_label)
        layout.addWidget(QLabel(f"Título: {titulo}", self))
        layout.addWidget(QLabel(f"Sinopsis: {sinopsis}", self))
        layout.addWidget(QLabel(f"Puntuación: {puntuacion}", self))
        layout.addWidget(QLabel(f"Actores: {', '.join(actores)}", self))
        layout.addWidget(QLabel(f"Género: {genero}", self))

        self.setLayout(layout)
