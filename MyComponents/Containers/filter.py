from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLineEdit, QListWidget, QSizePolicy
from MyComponents.MyButtons import filterButton


class FilterContainer:
    def __init__(self):
        self.filter_btn = filterButton()
        self.lineEdit = QLineEdit()
        self.filter_lst = QListWidget()

        self.filter_btn.setFixedSize(30, 30)

        self.lineEdit.setFixedHeight(30)
        self.lineEdit.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.lineEdit.setPlaceholderText("*.CATDrawing")

        filters = ["*.pdf", "*.CATProduct", "*.CATDrawing"]
        self.filter_lst.addItems(filters)

    def create(self):
        widget = QWidget()
        main_layout = QVBoxLayout()
        input_layout = QHBoxLayout()

        input_layout.addWidget(self.lineEdit)
        input_layout.addWidget(self.filter_btn)

        main_layout.addLayout(input_layout)
        main_layout.addWidget(self.filter_lst)

        widget.setLayout(main_layout)

        def addFilterAction():
            filter_value = self.lineEdit.text()
            self.filter_lst.addItem(filter_value)

        self.filter_btn.clicked.connect(addFilterAction)

        return widget
