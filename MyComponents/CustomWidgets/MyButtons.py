from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtWidgets import QPushButton, QSizePolicy


class ExtractButton(QPushButton):
    def __init__(self, text):
        super().__init__()
        self.setText(text)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.setFont(QFont("Myriad Pro", 17))
        self.setMaximumSize(1000, 100)
        self.setStyleSheet("""
            ExtractButton {
                background-color: #b5b5b5;
                color: #2D3047;
                border-radius: 5px;
                font-weight: bold;
                letter-spacing: 3px;
                margin: 5px;
            }
            ExtractButton:hover {
                border-style: outset;
                border-width: 4px;
                border-color: #fba300;
            }
            ExtractButton:pressed {
                border-style: inset;
                background-color: #bcbcbc;
                border-width: 4px 4px 5px 5px;
                border-color:  #fba300;
            }
        """)


class BrowseButton(QPushButton):
    def __init__(self):
        super().__init__()
        icon = QIcon("Resources/folder.png")
        self.setIcon(icon)
        self.setStyleSheet("""
            BrowseButton {
                background-color: #b5b5b5;
                color: #2D3047;
                border-radius: 5px;
            }
            BrowseButton:hover {
                border-style: outset;
                border-width: 2px;
                border-color: #fba300;
            }
            BrowseButton:pressed {
                border-style: inset;
                background-color: #bcbcbc;
                border-width: 2px 2px 3px 3px;
                border-color:  #fba300;
            }
        """)


class filterButton(QPushButton):
    def __init__(self):
        super().__init__()
        icon = QIcon("Resources/filter.png")
        self.setIcon(icon)
        self.setStyleSheet("""
            filterButton {
                background-color: #b5b5b5;
                color: #2D3047;
                border-radius: 5px;

            }
            filterButton:hover {
                border-style: outset;
                border-width: 2px;
                border-color: #fba300;
            }
            filterButton:pressed {
                border-style: inset;
                background-color: #bcbcbc;
                border-width: 2px 2px 3px 3px;
                border-color:  #fba300;
            }
        """)
