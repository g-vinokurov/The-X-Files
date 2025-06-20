
from PyQt6.QtWidgets import QApplication

from Ui.Widgets.Window import Window

if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()
