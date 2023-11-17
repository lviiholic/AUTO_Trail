import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import Ui_qurey

app=QApplication(sys.argv)
MainWindow = QMainWindow()
ui = Ui_qurey.Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())