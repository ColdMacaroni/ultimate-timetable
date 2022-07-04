from PySide6 import QtWidgets, QtCore
from model import Spell, SpellSlot, Day

app = QtWidgets.QApplication()


class SpellInfoWidget(QtWidgets.QWidget):
    def __init__(self, *args):
        super().__init__(*args)
        # TODO: Spellslot object

        self.spell_code_label = QtWidgets.QLabel(self)
        self.spell_name_label = QtWidgets.QLabel(self)

        self.teacher_name_label = QtWidgets.QLabel(self)

        self.time_label = QtWidgets.QLabel(self)
        self.initUI()

    def initUI(self):
        main_vbox = QtWidgets.QVBoxLayout()

        main_vbox.addWidget(self.spell_code_label)
        main_vbox.addWidget(self.spell_name_label)
        main_vbox.addWidget(self.teacher_name_label)
        main_vbox.addWidget(self.time_label)

        self.setLayout(main_vbox)


class TimetableMain(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # For picking days
        # self.day_combobox = QtWidgets.QComboBox(self)
        self.days_tabwidget = QtWidgets.QTabWidget(self)
        self.day_widgets = {
            day: QtWidgets.QWidget(self.days_tabwidget)
            for day in Day
        }

        # For setting if spell 5 exists
        self.spell5_checkbox = QtWidgets.QCheckBox("Spell 5", self)

        # For actually viewing the info
        self.spell_info = SpellInfoWidget(self)

        self.initUI()

    def initUI(self):
        self.setCentralWidget(QtWidgets.QWidget())
        self.setGeometry(QtCore.QRect(100, 100, 600, 500))

        # Populate tabwidget
        for name, widg in self.day_widgets.items():
            self.days_tabwidget.addTab(widg, str(name))

        # Put the tabs on the left so we dont need to scroll
        self.days_tabwidget.setTabPosition(
            QtWidgets.QTabWidget.TabPosition.West
        )

        # This is the main layout for the window
        hbox = QtWidgets.QHBoxLayout(self.centralWidget())

        # This will put the combo box and spell 5 checkbox next to each other
        left_vbox = QtWidgets.QVBoxLayout(self.centralWidget())

        # The stretch is because they look weird when right next to each other
        # header_hbox.addWidget(self.day_combobox)
        left_vbox.addWidget(self.spell5_checkbox)
        left_vbox.addWidget(self.days_tabwidget)

        hbox.addLayout(left_vbox)
        hbox.addWidget(self.spell_info)

        self.centralWidget().setLayout(hbox)
