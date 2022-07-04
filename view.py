from PySide6 import QtWidgets, QtCore
from model import SpellSlot, Day

app = QtWidgets.QApplication()


class SpellInfoWidget(QtWidgets.QWidget):
    def __init__(self, *args):
        super().__init__(*args)
        self.spell_slot = None

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

    # spell_slot has a setter unlike the other members because it is expected
    # to be set externally. The other members are widgets which should not be
    # replaced with other widgets. If you replace them, then its your problem.
    @property
    def spell_slot(self) -> SpellSlot:
        return self._spell_slot

    @spell_slot.setter
    def spell_slot(self, new):
        # We'll accept None in the cases where the spellslot hasnt
        # been selected, such as when creating a new SpellInfoWidget or
        # changing the tab in the main window.
        if not (isinstance(new, SpellSlot) or new is None):
            raise ValueError("spell_slot must be set to a SpellSlot object"
                             " or None")

        self._spell_slot = new


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
