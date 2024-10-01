import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton

from modelopeliculas import ModeloPeliculas
from vistapeliculas import UiMainWindow, DetallesPeliculaDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._ui = UiMainWindow()
        self._ui.setup_ui(self)

        self._modelo = ModeloPeliculas()

        self._ui._boton_buscar_pelicula.clicked.connect(self._buscar_pelicula)
        self._ui._boton_buscar_por_actores.clicked.connect(self._abrir_buscar_por_actores)
        self._ui._list_widget.itemClicked.connect(self._mostrar_detalles_pelicula)

    def _buscar_pelicula(self):
        nombre_pelicula = self._ui._line_edit.text()  # Cambiado aquí también
        self._ui._list_widget.clear()
        peliculas_encontradas = self._modelo.buscar_pelicula(nombre_pelicula)

        for pelicula in peliculas_encontradas:
            self._ui._list_widget.addItem(pelicula['titulo'])

    def _mostrar_detalles_pelicula(self, item):
        titulo_pelicula = item.text()
        pelicula = self._modelo.obtener_informacion_pelicula(titulo_pelicula)

        if pelicula:
            detalles_dialog = DetallesPeliculaDialog(pelicula, self)
            detalles_dialog.exec()

    def _abrir_buscar_por_actores(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Buscar por Actores")
        layout = QVBoxLayout(dialog)

        label = QLabel("Ingresa el nombre del actor:", dialog)
        layout.addWidget(label)

        actor_input = QLineEdit(dialog)
        layout.addWidget(actor_input)

        boton_buscar = QPushButton("Buscar", dialog)
        layout.addWidget(boton_buscar)

        boton_buscar.clicked.connect(lambda: self._buscar_por_actor(actor_input.text()))

        dialog.setLayout(layout)
        dialog.exec()

    def _buscar_por_actor(self, actor):
        dialog = QDialog(self)
        dialog.setWindowTitle("Resultados de la Búsqueda")
        layout = QVBoxLayout(dialog)

        peliculas_encontradas = self._modelo.buscar_por_actor(actor)
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