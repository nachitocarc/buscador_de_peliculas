from PySide6.QtCore import QSize, QRect, QCoreApplication, QMetaObject
from PySide6.QtWidgets import (QWidget, QGridLayout, QListWidget,
                               QPushButton, QLineEdit, QSpacerItem, QSizePolicy, QLabel, QStatusBar, QDialog,
                               QVBoxLayout, QMenuBar)


class UiMainWindow(object):
    def setup_ui(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"MainWindow")
        main_window.resize(800, 600)
        self.centralwidget = QWidget(main_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")

        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMaximumSize(QSize(16777215, 500))
        self.gridLayout.addWidget(self.listWidget, 2, 0, 1, 5)

        self.cargar_peliculas_iniciales()

        self.boton_buscar_por_actores = QPushButton(self.centralwidget)
        self.boton_buscar_por_actores.setObjectName(u"pushButton_2")
        self.gridLayout.addWidget(self.boton_buscar_por_actores, 0, 1, 1, 1)

        self.boton_buscar_pelicula = QPushButton(self.centralwidget)
        self.boton_buscar_pelicula.setObjectName(u"pushButton")
        self.gridLayout.addWidget(self.boton_buscar_pelicula, 0, 4, 1, 1)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout.addItem(self.horizontalSpacer, 1, 3, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 20))
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)

        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(main_window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        main_window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(main_window)
        self.statusbar.setObjectName(u"statusbar")
        main_window.setStatusBar(self.statusbar)

        self.retranslate_ui(main_window)
        QMetaObject.connectSlotsByName(main_window)

    def cargar_peliculas_iniciales(self):
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
            self.listWidget.addItem(pelicula)

    def retranslate_ui(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("MainWindow", u"Buscador de Películas", None))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)

        for i in range(self.listWidget.count()):
            item = self.listWidget.item(i)
            item.setText(QCoreApplication.translate("MainWindow", item.text(), None))

        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.boton_buscar_por_actores.setText(QCoreApplication.translate("MainWindow", u"Buscar por actores", None))
        self.boton_buscar_pelicula.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingresar nombre de película...", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Películas:", None))


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
