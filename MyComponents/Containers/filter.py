from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLineEdit, QListWidget, QSizePolicy
from MyComponents.MyButtons import filterButton


def createFilters():
    widget = QWidget()
    main_layout = QVBoxLayout()
    input_layout = QHBoxLayout()

    filter_btn = filterButton()
    filter_btn.setFixedSize(30, 30)

    lineEdit = QLineEdit()
    lineEdit.setFixedHeight(30)
    lineEdit.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
    lineEdit.setPlaceholderText("*.CATDrawing")

    filter_lst = QListWidget()
    filters = ["*.pdf", "*.CATProduct", "*.CATDrawing"]
    filter_lst.addItems(filters)

    input_layout.addWidget(lineEdit)
    input_layout.addWidget(filter_btn)

    main_layout.addLayout(input_layout)
    main_layout.addWidget(filter_lst)

    widget.setLayout(main_layout)
    return widget
