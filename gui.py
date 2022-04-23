from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(750, 250, 500, 500)
    win.setWindowTitle('YGO Card Search')

    win.show()
    sys.exit(app.exec_())

window()