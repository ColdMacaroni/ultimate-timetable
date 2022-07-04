from PySide6 import QtWidgets, QtCore
from model import SpellSlot, Day

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
        # self.day_combobox = QtWidgets.QComboBox(self)
        self.days_tabwidget = QtWidgets.QTabWidget(self)
        self.day_widgets = {str(day): QtWidgets.QWidget(self.days_tabwidget) for day in Day}

        # For setting if spell 5 exists
        self.spell5_checkbox = QtWidgets.QCheckBox("Spell 5", self)

        self.initUI()

    def initUI(self):
        self.setCentralWidget(QtWidgets.QWidget())
        self.setGeometry(QtCore.QRect(100, 100, 400, 500))

        # TODO: self.day_combobox.curentRowChanged.connect()
        # Populate tabwidget
        for name, widg in self.day_widgets.items():
            self.days_tabwidget.addTab(widg, name)
        
        # Put the tabs on the left so we dont need to scroll
        self.days_tabwidget.setTabPosition(QtWidgets.QTabWidget.TabPosition.West)

        # This is the main layout for the window
        hbox = QtWidgets.QHBoxLayout(self.centralWidget())

        # This will put the combo box and spell 5 checkbox next to each other
        left_vbox = QtWidgets.QVBoxLayout(self.centralWidget())

        # The stretch is because they look weird when right next to each other
        # header_hbox.addWidget(self.day_combobox)
        left_vbox.addWidget(self.spell5_checkbox)
        left_vbox.addWidget(self.days_tabwidget)

        hbox.addLayout(left_vbox)

        self.centralWidget().setLayout(hbox)
