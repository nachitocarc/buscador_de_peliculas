from PySide6.QtCore import QRect, QCoreApplication, QMetaObject, QSize
from PySide6.QtWidgets import (QWidget, QGridLayout, QListWidget,
                               QPushButton, QLineEdit, QSpacerItem, QSizePolicy, QLabel, QStatusBar, QDialog,
                               QVBoxLayout, QMenuBar)
from PySide6.QtGui import QPixmap


class UiMainWindow(object):
    def setup_ui(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"MainWindow")
        main_window.resize(800, 600)
        self._central_widget = QWidget(main_window)
        self._central_widget.setObjectName(u"centralwidget")
        self._grid_layout = QGridLayout(self._central_widget)
        self._grid_layout.setObjectName(u"gridLayout")

        self.list_widget = QListWidget(self._central_widget)
        self.list_widget.setObjectName(u"listWidget")
        self.list_widget.setMaximumSize(QSize(16777215, 500))
        self._grid_layout.addWidget(self.list_widget, 2, 0, 1, 5)

        self.boton_buscar_por_actores = QPushButton(self._central_widget)
        self.boton_buscar_por_actores.setObjectName(u"pushButton_2")
        self._grid_layout.addWidget(self.boton_buscar_por_actores, 0, 1, 1, 1)

        self.boton_buscar_pelicula = QPushButton(self._central_widget)
        self.boton_buscar_pelicula.setObjectName(u"pushButton")
        self._grid_layout.addWidget(self.boton_buscar_pelicula, 0, 4, 1, 1)

        self.line_edit = QLineEdit(self._central_widget)
        self.line_edit.setObjectName(u"lineEdit")
        self._grid_layout.addWidget(self.line_edit, 0, 3, 1, 1)

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

    def _retranslate_ui(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("MainWindow", u"Buscador de Películas", None))
        __sorting_enabled = self.list_widget.isSortingEnabled()
        self.list_widget.setSortingEnabled(False)

        for i in range(self.list_widget.count()):
            item = self.list_widget.item(i)
            item.setText(QCoreApplication.translate("MainWindow", item.text(), None))

        self.list_widget.setSortingEnabled(__sorting_enabled)

        self.boton_buscar_por_actores.setText(QCoreApplication.translate("MainWindow", u"Buscar por actores", None))
        self.boton_buscar_pelicula.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.line_edit.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Ingresar nombre de película...", None))
        self._label.setText(QCoreApplication.translate("MainWindow", u"Películas:", None))


class DetallesPeliculaDialog(QDialog):
    def __init__(self, pelicula, parent=None):
        super().__init__(parent)
        self.setWindowTitle(pelicula['titulo'])

        layout = QVBoxLayout(self)

        poster_label = QLabel(self)
        poster_pixmap = QPixmap(pelicula["poster"])

        if poster_pixmap.isNull():
            print("Error: No se pudo cargar la imagen.")
            poster_label.setText("No se pudo cargar el póster.")
        else:
            scaled_pixmap = poster_pixmap.scaled(350, 400)
            poster_label.setPixmap(scaled_pixmap)

        layout.addWidget(poster_label)

        titulo_label = QLabel(f"Título: {pelicula['titulo']}", self)
        layout.addWidget(titulo_label)

        sinopsis_label = QLabel(f"Sinopsis: {pelicula['sinopsis']}", self)
        layout.addWidget(sinopsis_label)

        puntuacion_label = QLabel(f"Puntuación: {pelicula['puntuacion']}", self)
        layout.addWidget(puntuacion_label)

        self.setLayout(layout)
