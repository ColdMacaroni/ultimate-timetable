from PySide6 import QtWidgets, QtCore
from model import SpellSlot, Day

app = QtWidgets.QApplication()


class SpellInfoWidget(QtWidgets.QWidget):
    """Widget that holds the information relating to the clicked spell"""
    def __init__(self, *args):
        super().__init__(*args)
        self.container_widget = QtWidgets.QWidget(self)

        self.spell_slot = None

        self.spell_name_label = QtWidgets.QLabel(self.container_widget)
        self.spell_code_label = QtWidgets.QLabel(self.container_widget)

        self.room_label = QtWidgets.QLabel(self.container_widget)

        self.teacher_name_label = QtWidgets.QLabel(self.container_widget)

        self.time_label = QtWidgets.QLabel(self.container_widget)
        # TODO: Combobox for attendance
        # TODO: listwidget for homework (not needed. Do only if need to flex)
        self.initUI()

    def initUI(self):
        holder_layout = QtWidgets.QVBoxLayout(self)
        vbox = QtWidgets.QVBoxLayout(self.container_widget)

        vbox.addWidget(self.spell_code_label)
        vbox.addWidget(self.spell_name_label)
        vbox.addWidget(self.room_label)
        vbox.addWidget(self.teacher_name_label)
        vbox.addWidget(self.time_label)

        # These keeps all children compact and stops them from being stretched
        vbox.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)

        self.container_widget.setLayout(vbox)
        holder_layout.addLayout(vbox)
        self.setLayout(holder_layout)

    def clear(self):
        # We'll go through each attribute of this class and clear them if they
        # are a clearable type. Not using hasattr because some clearing
        # behaviour may be unwanted. Like clearing a dictionary

        # Types that can be cleared
        clearable = (QtWidgets.QLabel, QtWidgets.QListWidget)

        # Expression for going through this objects attributes -> vars(self)
        # learnt from a comment by juanpa.arrivillaga in
        # https://stackoverflow.com/a/67220630
        for value in vars(self).values():
            if any(map(lambda type_: isinstance(value, type_), clearable)):
                value.clear()

    ##
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
    """The main window of the timetable. Holds all other widgets"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # For picking days
        # self.day_combobox = QtWidgets.QComboBox(self)
        self.days_tabwidget = QtWidgets.QTabWidget(self)
        self.day_widgets = {
            day: QtWidgets.QWidget(self.days_tabwidget)
            for day in Day
        }

        # TODO! Replace all references to spell 5 with last spell
        # For setting if spell 5 exists
        self.spell5_checkbox = QtWidgets.QCheckBox("Spell 5", self)

        # For actually viewing the info
        self.spell_info = SpellInfoWidget(self)

        self.initUI()

    def initUI(self):
        self.setCentralWidget(QtWidgets.QWidget())
        self.setGeometry(QtCore.QRect(100, 100, 440, 500))

        # Populate tabwidget
        for name, widg in self.day_widgets.items():
            self.days_tabwidget.addTab(widg, str(name))

        # Put the tabs on the left so we dont need to scroll
        self.days_tabwidget.setTabPosition(
            QtWidgets.QTabWidget.TabPosition.West
        )

        # This is the main layout for the window
        hbox = QtWidgets.QHBoxLayout(self.centralWidget())

        # This will put the checkbox above the tabwidget
        left_vbox = QtWidgets.QVBoxLayout(self.centralWidget())

        # The stretch is because they look weird when right next to each other
        # header_hbox.addWidget(self.day_combobox)
        left_vbox.addWidget(self.spell5_checkbox)
        left_vbox.addWidget(self.days_tabwidget)

        # For setting the ratio of each widget
        # https://stackoverflow.com/a/26897934
        hbox.addLayout(left_vbox, 2)
        hbox.addWidget(self.spell_info, 3)

        self.centralWidget().setLayout(hbox)
