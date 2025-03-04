import sys
from PySide6.QtWidgets import QApplication
from controlador_peliculas import Controlador
from modelo_peliculas import Catalogo

if __name__ == "__main__":
    app = QApplication(sys.argv)
    modelo = Catalogo("peliculas.json")
    ventana_principal = Controlador(modelo)
    ventana_principal.show()

    sys.exit(app.exec())
