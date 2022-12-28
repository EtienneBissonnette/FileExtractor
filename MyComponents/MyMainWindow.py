from PyQt6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout
from MyComponents.CustomWidgets.MyButtons import ExtractButton
from MyComponents.Containers.browse import BrowseContainer
from MyComponents.Containers.filter import FilterContainer
from MyFunctions.extraction import extraction


class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Folder Extractor")
        self.setMinimumSize(600, 300)
        self.setMaximumSize(900, 400)

        main_widget = QWidget()

        main_layout = QVBoxLayout()
        btm_layout = QHBoxLayout()

        extract_btn = ExtractButton("EXTRACT")

        browseContainer = BrowseContainer()
        browse_input = browseContainer.create()

        filterContainer = FilterContainer()
        filter_input = filterContainer.create()

        main_layout.addWidget(browse_input)
        btm_layout.addWidget(filter_input)
        btm_layout.addWidget(extract_btn)

        def extractAction():
            browse_path = browseContainer.lineEdit.text()
            filter_list = filterContainer.filter_lst

            used_filters = []
            for i in range(filter_list.count()):
                used_filters.append(filter_list.item(i).text())

            extraction(browse_path,used_filters)

        extract_btn.clicked.connect(extractAction)

        main_layout.addLayout(btm_layout)

        main_widget.setLayout(main_layout)

        self.setCentralWidget(main_widget)
        self.show()
