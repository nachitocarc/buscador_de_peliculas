import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton

from modelopeliculas import ModeloPeliculas
from vistapeliculas import UiMainWindow, DetallesPeliculaDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = UiMainWindow()
        self.ui.setup_ui(self)

        self.modelo = ModeloPeliculas()

        self.ui.boton_buscar_pelicula.clicked.connect(self.buscar_pelicula)
        self.ui.boton_buscar_por_actores.clicked.connect(self.abrir_buscar_por_actores)
        self.ui.listWidget.itemClicked.connect(self.mostrar_detalles_pelicula)

    def buscar_pelicula(self):
        nombre_pelicula = self.ui.lineEdit.text()
        self.ui.listWidget.clear()
        peliculas_encontradas = self.modelo.buscar_pelicula(nombre_pelicula)

        for pelicula in peliculas_encontradas:
            self.ui.listWidget.addItem(pelicula['titulo'])

    def mostrar_detalles_pelicula(self, item):
        titulo_pelicula = item.text()
        pelicula = self.modelo.obtener_informacion_pelicula(titulo_pelicula)

        if pelicula:
            detalles_dialog = DetallesPeliculaDialog(pelicula, self)
            detalles_dialog.exec()

    def abrir_buscar_por_actores(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Buscar por Actores")
        layout = QVBoxLayout(dialog)

        label = QLabel("Ingresa el nombre del actor:", dialog)
        layout.addWidget(label)

        actor_input = QLineEdit(dialog)
        layout.addWidget(actor_input)

        boton_buscar = QPushButton("Buscar", dialog)
        layout.addWidget(boton_buscar)

        boton_buscar.clicked.connect(lambda: self.buscar_por_actor(actor_input.text()))

        dialog.setLayout(layout)
        dialog.exec()

    def buscar_por_actor(self, actor):
        dialog = QDialog(self)
        dialog.setWindowTitle("Resultados de la Búsqueda")
        layout = QVBoxLayout(dialog)

        peliculas_encontradas = self.modelo.buscar_por_actor(actor)
        if not peliculas_encontradas:
            label = QLabel("No se encontraron películas para este actor.", dialog)
            layout.addWidget(label)
        else:
            for pelicula in peliculas_encontradas:
                layout.addWidget(QLabel(pelicula, dialog))

        dialog.setLayout(layout)
        dialog.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
