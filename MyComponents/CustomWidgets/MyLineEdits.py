from PyQt6.QtWidgets import QLineEdit


class BrowseLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Enable drag and drop
        self.setDragEnabled(True)

    def dragEnterEvent(self, event):
        # Accept the drag and drop event if the data is a file
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        # Get the file path from the dropped data
        file_path = event.mimeData().urls()[0].toLocalFile()

        # Set the text of the line edit to the file path
        self.setText(file_path)
