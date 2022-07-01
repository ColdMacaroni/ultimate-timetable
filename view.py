from PySide6 import QtWidgets
from model import SpellSlot
app = QtWidgets.QApplication()


class SpellWidget(QtWidgets.QFrame):
    def __init__(self, spell_slot: SpellSlot, *args):
        super().__init__(*args)

        self.spell_slot = spell_slot
        self.spell_code_label = QtWidgets.QLabel(self)

        self.spell_start = QtWidgets.QLabel(self)

        self.spell_end = QtWidgets.QLabel(self)
        self.initUI()

    def initUI(self):
        self.setFrameStyle(QtWidgets.QFrame.StyledPanel)
        main_vbox = QtWidgets.QVBoxLayout()

        main_vbox.addWidget(self.spell_code_label)
        main_vbox.addWidget(self.spell_end)
        main_vbox.addWidget(self.spell_start)

        self.setLayout(main_vbox)


class TimetableMain(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # For picking days
        self.day_combobox = QtWidgets.QComboBox(self)

        # For setting if spell 5 exists
        self.spell5_checkbox = QtWidgets.QCheckBox("Spell 5", self)

        self.initUI()

    def initUI(self):
        self.setCentralWidget(QtWidgets.QWidget())

        # This is the main layout for the window
        vbox = QtWidgets.QVBoxLayout(self.centralWidget())

        vbox.addWidget(self.day_combobox)
        vbox.addWidget(self.spell5_checkbox)

        self.centralWidget().setLayout(vbox)
