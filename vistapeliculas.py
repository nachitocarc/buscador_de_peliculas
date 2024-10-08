from PySide6.QtCore import QSize, QRect, QCoreApplication, QMetaObject
from PySide6.QtWidgets import (QWidget, QGridLayout, QListWidget,
                               QPushButton, QLineEdit, QSpacerItem, QSizePolicy, QLabel, QStatusBar, QDialog,
                               QVBoxLayout, QMenuBar)


class UiMainWindow(object):
    def setup_ui(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"MainWindow")
        main_window.resize(800, 600)
        self._central_widget = QWidget(main_window)
        self._central_widget.setObjectName(u"centralwidget")
        self._grid_layout = QGridLayout(self._central_widget)
        self._grid_layout.setObjectName(u"gridLayout")

        self._list_widget = QListWidget(self._central_widget)
        self._list_widget.setObjectName(u"listWidget")
        self._list_widget.setMaximumSize(QSize(16777215, 500))
        self._grid_layout.addWidget(self._list_widget, 2, 0, 1, 5)

        self._cargar_peliculas_iniciales()

        self._boton_buscar_por_actores = QPushButton(self._central_widget)
        self._boton_buscar_por_actores.setObjectName(u"pushButton_2")
        self._grid_layout.addWidget(self._boton_buscar_por_actores, 0, 1, 1, 1)

        self._boton_buscar_pelicula = QPushButton(self._central_widget)
        self._boton_buscar_pelicula.setObjectName(u"pushButton")
        self._grid_layout.addWidget(self._boton_buscar_pelicula, 0, 4, 1, 1)

        self._line_edit = QLineEdit(self._central_widget)
        self._line_edit.setObjectName(u"lineEdit")
        self._grid_layout.addWidget(self._line_edit, 0, 3, 1, 1)

        self._horizontal_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self._grid_layout.addItem(self._horizontal_spacer, 1, 3, 1, 1)

        self._label = QLabel(self._central_widget)
        self._label.setObjectName(u"label")
        self._label.setMaximumSize(QSize(16777215, 20))
        self._grid_layout.addWidget(self._label, 1, 1, 1, 1)

        main_window.setCentralWidget(self._central_widget)
        self._menu_bar = QMenuBar(main_window)
        self._menu_bar.setObjectName(u"menubar")
        self._menu_bar.setGeometry(QRect(0, 0, 800, 22))
        main_window.setMenuBar(self._menu_bar)
        self._status_bar = QStatusBar(main_window)
        self._status_bar.setObjectName(u"statusbar")
        main_window.setStatusBar(self._status_bar)

        self._retranslate_ui(main_window)
        QMetaObject.connectSlotsByName(main_window)

    def _cargar_peliculas_iniciales(self):
        peliculas_iniciales = [
            "Son como niños",
            "Titanic",
            "Mi primer beso",
            "Chiquito pero peligroso",
            "Violet y Finch",
            "El hijo de la novia",
            "Super cool",
            "Un espía y medio",
            "Entre la vida y la muerte"
        ]
        for pelicula in peliculas_iniciales:
            self._list_widget.addItem(pelicula)

    def _retranslate_ui(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("MainWindow", u"Buscador de Películas", None))
        __sorting_enabled = self._list_widget.isSortingEnabled()
        self._list_widget.setSortingEnabled(False)

        for i in range(self._list_widget.count()):
            item = self._list_widget.item(i)
            item.setText(QCoreApplication.translate("MainWindow", item.text(), None))

        self._list_widget.setSortingEnabled(__sorting_enabled)

        self._boton_buscar_por_actores.setText(QCoreApplication.translate("MainWindow", u"Buscar por actores", None))
        self._boton_buscar_pelicula.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self._line_edit.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Ingresar nombre de película...", None))
        self._label.setText(QCoreApplication.translate("MainWindow", u"Películas:", None))

    @property
    def boton_buscar_pelicula(self):
        return self._boton_buscar_pelicula

    @property
    def boton_buscar_por_actores(self):
        return self._boton_buscar_por_actores

    @property
    def list_widget(self):
        return self._list_widget


class DetallesPeliculaDialog(QDialog):
    def __init__(self, pelicula, parent=None):
        super().__init__(parent)
        self.setWindowTitle(pelicula['titulo'])
        self.setGeometry(100, 100, 400, 600)

        layout = QVBoxLayout()

        titulo_label = QLabel(f"Título: {pelicula['titulo']}", self)
        layout.addWidget(titulo_label)

        sinopsis_label = QLabel(f"Sinopsis: {pelicula['sinopsis']}", self)
        layout.addWidget(sinopsis_label)

        actores_label = QLabel(f"Actores: {', '.join(pelicula['actores'])}", self)
        layout.addWidget(actores_label)

        puntuacion_label = QLabel(f"Puntuación: {pelicula['puntuacion']}", self)
        layout.addWidget(puntuacion_label)

        self.setLayout(layout)
