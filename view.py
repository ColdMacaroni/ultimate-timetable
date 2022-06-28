from PySide6 import QtWidgets

app = QtWidgets.QApplication()

class TimetableMain(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # For picking days
        self.day_combobox = QtWidgets.QComboBox(self)
        
        # For setting if spell 5 exists
        self.spell5_checkbox = QtWidgets.QCheckBox("Spell 5", self)
        
        self.initUI()

    def initUI(self):
        self.setCentralWidget(QtWidgets)

        # This is the main layout for the window
        vbox = QtWidgets.QVBoxLayout(self)

        vbox.addWidget(self.day_combobox)
        vbox.addWidget(self.spell5_checkbox)
        
        self.centralWidget().setLayout(vbox)
    
