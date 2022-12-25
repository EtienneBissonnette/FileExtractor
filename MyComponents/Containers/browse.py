from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLineEdit, QSizePolicy
from MyComponents.MyButtons import BrowseButton


def createBrowse(): #TODO: ADD PROCESS TO THE CLICK SIGNAL ON THE BROWSE BTN
    widget = QWidget()
    layout = QHBoxLayout()

    browse_btn = BrowseButton()
    browse_btn.setFixedSize(30, 30)

    lineEdit = QLineEdit()
    lineEdit.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
    lineEdit.setFixedHeight(30)
    lineEdit.setPlaceholderText("C:/ActiveUser/Downloads/Folder.zip")

    layout.addWidget(lineEdit)
    layout.addWidget(browse_btn)

    widget.setLayout(layout)
    widget.setFixedHeight(45)

    # browse_btn.clicked.connect()

    return widget




