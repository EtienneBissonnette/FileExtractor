from PyQt6.QtWidgets import QApplication
from MyComponents.MyMainWindow import MyMainWindow


app = QApplication([])
window = MyMainWindow()

if __name__ == '__main__':

    app.exec()
