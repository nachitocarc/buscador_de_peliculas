# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nacho.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject)
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (QGridLayout, QLabel, QLineEdit,
                               QPushButton, QStatusBar, QWidget, QListWidget, QDialog, QVBoxLayout)


class UiMainWindow(object):
    def _setup_ui(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"MainWindow")
        main_window.resize(800, 600)
        self.centralwidget = QWidget(main_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")

        self.boton_buscar_pelicula = QPushButton(self.centralwidget)
        self.boton_buscar_pelicula.setObjectName(u"pushButton_2")
        self.gridLayout.addWidget(self.boton_buscar_pelicula, 0, 3, 1, 1)

        self.line_edit = QLineEdit(self.centralwidget)
        self.line_edit.setObjectName(u"lineEdit")
        self.gridLayout.addWidget(self.line_edit, 0, 2, 1, 1)

        self.boton_buscar_por_actores = QPushButton(self.centralwidget)
        self.boton_buscar_por_actores.setObjectName(u"pushButton")
        self.gridLayout.addWidget(self.boton_buscar_por_actores, 0, 0, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.catalogo = QListWidget(self.centralwidget)
        self.catalogo.setObjectName(u"listView")
        self.gridLayout.addWidget(self.catalogo, 2, 0, 1, 4)

        main_window.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(main_window)
        self.statusbar.setObjectName(u"statusbar")
        main_window.setStatusBar(self.statusbar)

        self.__retranslateui(main_window)
        QMetaObject.connectSlotsByName(main_window)

    def __retranslateui(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("MainWindow", u"Buscador de peliculas", None))
        self.boton_buscar_pelicula.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.line_edit.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Introduzca el nombre de la pelicula", None))
        self.boton_buscar_por_actores.setText(QCoreApplication.translate("MainWindow", u"Buscar por actores", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Pelicula:", None))


class DetallesPeliculaDialog(QDialog):
    def __init__(self, pelicula, parent=None):
        super().__init__(parent)
        self.setWindowTitle(pelicula['titulo'])

        layout = QVBoxLayout(self)

        poster_label = QLabel(self)
        poster_pixmap = QPixmap(pelicula["poster"])

        if poster_pixmap.isNull():
            poster_label.setText("No se pudo cargar el póster.")
        else:
            scaled_pixmap = poster_pixmap.scaled(200, 300)
            poster_label.setPixmap(scaled_pixmap)

        layout.addWidget(poster_label)

        titulo_label = QLabel(f"Título: {pelicula['titulo']}", self)
        layout.addWidget(titulo_label)

        sinopsis_label = QLabel(f"Sinopsis: {pelicula['sinopsis']}", self)
        layout.addWidget(sinopsis_label)

        puntuacion_label = QLabel(f"Puntuación: {pelicula['puntuacion']}", self)
        layout.addWidget(puntuacion_label)

        actores_label = QLabel(f"Actores: {', '.join(pelicula['actores'])}", self)
        layout.addWidget(actores_label)

        genero_label = QLabel(f"Genero: {pelicula['género']}", self)
        layout.addWidget(genero_label)

        self.setLayout(layout)
