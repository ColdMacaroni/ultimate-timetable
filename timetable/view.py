from PySide6 import QtWidgets, QtCore
from timetable.model import SpellSlot, Day, AttendanceCode

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

        # We need a specific widget for the forms because we cant hide a layout
        # and clearing would mean having to always re-add all the widgets again
        self.form_widget = QtWidgets.QWidget(self.container_widget)
        self.attendance_combobox = QtWidgets.QComboBox(self.form_widget)

        self.initUI()

    def initUI(self):
        """
        Set up layouts and functionality of all the widgets
        """
        holder_layout = QtWidgets.QVBoxLayout(self)
        vbox = QtWidgets.QVBoxLayout(self.container_widget)

        vbox.addWidget(self.spell_code_label)
        vbox.addWidget(self.spell_name_label)
        vbox.addWidget(self.room_label)
        vbox.addWidget(self.teacher_name_label)
        vbox.addWidget(self.time_label)

        form_layout = QtWidgets.QFormLayout(self.container_widget)

        # Populate the combobox
        self.attendance_combobox.addItems([str(code)
                                           for code in AttendanceCode])
        form_layout.addRow("Attendance: ", self.attendance_combobox)

        self.form_widget.setLayout(form_layout)
        vbox.addWidget(self.form_widget)

        # These keeps all children compact and stops them from being stretched
        vbox.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)

        self.container_widget.setLayout(vbox)
        holder_layout.addLayout(vbox)
        self.setLayout(holder_layout)

    def clear(self):
        """
        This method makes all the children of this widget practically invisible
        Use this method insterad of .hide() to not mess up the layout.
        """
        # Whitelist of types with a safe .clear() method.
        # We're not using a blanket hasattr("clear") as it may have unwanted
        # effects on certain members. Like dictionaries or lists.
        clearable = (QtWidgets.QLabel, QtWidgets.QListWidget)

        # Expression for going through this object's attributes: vars(self)
        # learnt from a comment by juanpa.arrivillaga on
        # https://stackoverflow.com/a/67220630
        for value in vars(self).values():
            if any(map(lambda type_: isinstance(value, type_), clearable)):
                value.clear()

        # We dont want to clear the combobox because its values are the same
        # for all the spells. We'll just hide it and reshow it when a new
        # spell is shown
        self.form_widget.hide()

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
            raise ValueError(
                "spell_slot must be set to a SpellSlot object or None"
            )

        self._spell_slot = new


class TimetableMain(QtWidgets.QMainWindow):
    """The main window of the timetable. Holds all other widgets"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.days_tabwidget = QtWidgets.QTabWidget(self)
        self.day_widgets = {
            day: QtWidgets.QWidget(self.days_tabwidget)
            for day in Day
        }

        self.spell5_checkbox = QtWidgets.QCheckBox("Spell 5", self)

        self.spell_info = SpellInfoWidget(self)

        self.initUI()

    def initUI(self):
        """
        Set up layouts and functionality of all the widgets
        """
        self.setCentralWidget(QtWidgets.QWidget())
        self.setGeometry(QtCore.QRect(100, 100, 440, 500))

        # Populate tabwidget
        for name, widg in self.day_widgets.items():
            self.days_tabwidget.addTab(widg, str(name))

        # Put the tabs on the left so we dont need to scroll due to the small
        # horizontal size
        self.days_tabwidget.setTabPosition(
            QtWidgets.QTabWidget.TabPosition.West
        )

        # Make sure spell info isnt showing when we start as there is
        # nothing selected
        self.spell_info.clear()

        # This is the main layout for the window
        hbox = QtWidgets.QHBoxLayout(self.centralWidget())

        # This vbox will put the checkbox above the tabwidget
        left_vbox = QtWidgets.QVBoxLayout(self.centralWidget())

        left_vbox.addWidget(self.spell5_checkbox)
        left_vbox.addWidget(self.days_tabwidget)

        # For setting the ratio of each widget
        # https://stackoverflow.com/a/26897934
        hbox.addLayout(left_vbox, 2)
        hbox.addWidget(self.spell_info, 3)

        self.centralWidget().setLayout(hbox)
