from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLineEdit, QSizePolicy, QFileDialog
from MyComponents.MyButtons import BrowseButton


class BrowseContainer:
    def __init__(self):
        self.lineEdit = QLineEdit()
        self.browse_btn = BrowseButton()

        self.browse_btn.setFixedSize(30, 30)

        self.lineEdit.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.lineEdit.setFixedHeight(30)
        self.lineEdit.setPlaceholderText("C:/ActiveUser/Downloads/Folder.zip")

    def create(self):
        widget = QWidget()
        layout = QHBoxLayout()

        layout.addWidget(self.lineEdit)
        layout.addWidget(self.browse_btn)

        widget.setLayout(layout)
        widget.setFixedHeight(45)

        def browseAction():
            file_path, _ = QFileDialog.getOpenFileName()
            self.lineEdit.setText(file_path)

        self.browse_btn.clicked.connect(browseAction)

        return widget
