import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import Ui_query

app=QApplication(sys.argv)
MainWindow = QMainWindow()
ui = Ui_query.Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())