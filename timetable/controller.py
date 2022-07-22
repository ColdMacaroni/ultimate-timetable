from timetable import view
from timetable import model

import json

# For dealing with spell slots
FREE_SPELL_CODE = "FREE"


class SpellInfoController:
    def __init__(self, spell_info_widget: view.SpellInfoWidget):
        self.spell_info_widget = spell_info_widget

        self.spell_info_widget.attendance_combobox.currentTextChanged\
            .connect(self.attendance_combobox_currentTextChanged)

    def attendance_combobox_currentTextChanged(self, text):
        """
        Sets the attendance code of the current spellslot according to the
        combobox's text
        """
        code = model.AttendanceCode.from_str(text)

        self.spell_info_widget.spell_slot.attendance = code

    def update_labels(self, spell_slot: view.SpellSlot):
        """Changes the labels of this controller's info widget to match the
        given spell slot"""
        # Form is hidden on certain cases (e.g. spell 5 disabled while looking
        # at its info), we need to make sure it is shown
        self.spell_info_widget.form_widget.show()

        # These widgets are visible regardless of the type of spell
        self.spell_info_widget.spell_slot = spell_slot

        self.spell_info_widget.spell_code_label.setText(
            f"Code: {spell_slot.spell.class_code}"
        )
        self.spell_info_widget.spell_name_label.setText(
            f"Class name: {spell_slot.spell.class_name}"
        )

        self.spell_info_widget.attendance_combobox.setCurrentText(
            str(self.spell_info_widget.spell_slot.attendance)
        )

        # These dont have any info if the spells are free
        if spell_slot.spell.class_code != FREE_SPELL_CODE:
            self.spell_info_widget.teacher_name_label.show()
            self.spell_info_widget.teacher_name_label.setText(
                f"Teacher: {spell_slot.spell.teacher_name} "
                f"({spell_slot.spell.teacher_code})"
            )

            self.spell_info_widget.room_label.show()
            self.spell_info_widget.room_label.setText(
                f"Room: {spell_slot.spell.class_room}"
            )

        # We shouldnt show these on free spells
        else:
            self.spell_info_widget.teacher_name_label.hide()
            self.spell_info_widget.teacher_name_label.setText("")

            self.spell_info_widget.room_label.hide()
            self.spell_info_widget.room_label.setText("")

        self.spell_info_widget.time_label.setText(
            f"Duration: {spell_slot.start} - {spell_slot.end}"
        )


class TimetableController:
    def __init__(self, timetable_window: view.TimetableMain,
                 spell_dict: dict, times_dict: dict):
        self.timetable_window = timetable_window
        self.spell_dict = spell_dict
        self.times_dict = times_dict
        self.spell_info_controller = SpellInfoController(
            self.timetable_window.spell_info
        )

        # TODO: Add to testing table how invalid and boundary jsons behave
        self.spells = self.create_spells(self.spell_dict["spells"])

        self.day_spells = self.create_day_spells(
            self.spells,
            self.spell_dict["days"],
            self.times_dict
        )

        self.timetable_window.spell5_checkbox.setChecked(True)
        self.timetable_window.spell5_checkbox.stateChanged.connect(
            self.tw_spell5_checkbox_stateChanged
        )

        self.populate_tabs()

    @staticmethod
    def create_spells(spells_dict) -> dict[str, model.Spell]:
        """Creates Spell objects from the dictionary given"""
        spells = dict()

        for key, val in spells_dict.items():
            if val is not None:
                spell = model.Spell(**val)

            # Nones are free spells, they are None and not just another spell
            # because two types(keys) of spells can be free. And because they
            # have the same format

            # I'm not using a singleton because if they for example take up a
            # sixth spell, it would also affect the free spell on wednesdays
            # which is different.
            else:
                spell = model.Spell("Free Spell", FREE_SPELL_CODE, "", "", "")

            spells[key] = spell

        return spells

    @staticmethod
    def create_day_spells(
            spells: dict[str, model.Spell],
            spell_order: dict[str, list[str]],
            spell_times: dict[str, list[dict[str, list[int, int]]]]
            ) -> dict[str, model.DaySpells]:
        """
        This function creates SpellSlot objects and creates a DaySpells
        object from them.
        """
        # The final dictionary to be returned
        day_spells = dict()

        # These will be considered the only valid day keys.
        # Done this way so we dont accept any errors in the json files
        days = tuple(model.Day.str_dict.keys())

        for day in days:
            spell_slots = list()

            # Grab the idx as well to index the spell_times dict correctly
            for idx, spell_id in enumerate(spell_order[day]):
                spell = spells[spell_id]
                times_dict = spell_times[day][idx]

                # Create time objects
                time_start = model.Time(*times_dict["start"])
                time_end = model.Time(*times_dict["end"])

                spell_slots.append(
                    model.SpellSlot(
                        spell, time_start, time_end,
                        model.AttendanceCode.UNKNOWN
                    )
                )

            # Will keep as a string so its easier to work with combobox
            day_spells[day] = model.DaySpells(
                model.Day.from_str(day), spell_slots
            )

        return day_spells

    # TODO! Replace all references to spell 5 with last spell
    def tw_spell5_checkbox_stateChanged(self, state):
        """
        Sets the bool in DaySpell depending on the checkbox's state
        tw stands for timetable_window
        """
        # 0 is unchecked, checked is 2.
        # 1 is for half checked in tri state checkboxes
        if state == 2:
            model.DaySpells.spell_five = True

        elif state == 0:
            model.DaySpells.spell_five = False

        else:
            raise ValueError("Invalid checkbox state")

        # Make last button disappear or appear depending
        for day, tab in self.timetable_window.day_widgets.items():
            vbox = tab.layout()

            # In the rare case that the layout is empty
            if vbox.count() == 0:
                continue

            last_idx = vbox.count() - 1

            # Find the last button
            # We do it this way so we can add spacers and stuff at the end
            while not isinstance(
                    button := vbox.itemAt(last_idx).widget(),
                    view.QtWidgets.QPushButton
                    ):
                last_idx -= 1

                # This would happen if there isnt a button.
                # Just dont do anything
                if last_idx == -1:
                    break

            # We need to do it out here as well so we can continue the for loop
            if last_idx == -1:
                continue

            if model.DaySpells.spell_five:
                button.show()
            else:
                button.hide()

                # We dont want to keep showing the info for a spell that doesnt
                # exist. We'll check if the current displayed is the same as
                # the last one. And if it is, we'll just clear the information
                last_spell = self.day_spells[str(day).lower()].spell_slots[-1]
                if self.timetable_window.spell_info.spell_slot is last_spell:
                    self.timetable_window.spell_info.clear()

    def populate_tabs(self):
        """Adds buttons for all the spells on a day tab"""
        for day in model.Day:
            widget = self.timetable_window.day_widgets[day]
            day_spell = self.day_spells[str(day).lower()]

            vbox = view.QtWidgets.QVBoxLayout(widget)

            for spell_slot in day_spell.spell_slots:
                button = view.QtWidgets.QPushButton(widget)
                button.setText(
                    f"{spell_slot.spell.class_code}\n" +
                    (
                        # This doesnt show the room if the spell is free
                        # The newline is keep so all have the same height
                        "\n" if spell_slot.spell.class_code == FREE_SPELL_CODE
                        else f"Room {spell_slot.spell.class_room}\n"
                    ) +
                    f"{spell_slot.start} - {spell_slot.end}"
                )

                spell_slot.connect_with_self(
                    button.clicked,
                    self.spell_info_controller.update_labels
                )

                vbox.addWidget(button)

            widget.setLayout(vbox)

    def run(self):
        """This method makes the whole Qt stuff appear"""
        self.timetable_window.show()
        view.app.exec()
