from PySide6 import QtWidgets

app = QtWidgets.QApplication()

class TimetableMain(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
