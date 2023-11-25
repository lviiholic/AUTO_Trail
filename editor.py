import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import e2

app=QApplication(sys.argv)
MainWindow = QMainWindow()
ui = e2.Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())