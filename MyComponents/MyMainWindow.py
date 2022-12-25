from PyQt6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QSizePolicy, QFileDialog
from MyComponents.MyButtons import ExtractButton, BrowseButton
from MyComponents.Containers.browse import createBrowse
from MyComponents.Containers.filter import createFilters

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Folder Extractor")
        self.setMinimumSize(600,300)
        self.setMaximumSize(900,400)

        main_widget = QWidget()

        main_layout = QVBoxLayout()
        btm_layout = QHBoxLayout()

        extract_btn= ExtractButton("EXTRACT")
        browse_input = createBrowse()
        filter_input = createFilters()

        main_layout.addWidget(browse_input)
        btm_layout.addWidget(filter_input)
        btm_layout.addWidget(extract_btn)


        main_layout.addLayout(btm_layout)

        main_widget.setLayout(main_layout)

        self.setCentralWidget(main_widget)
        self.show()



