import view
import model
import json


class SpellInfoController:
    def __init__(self, spell_info_widget: view.SpellInfoWidget):
        self.spell_info_widget = spell_info_widget

    # TODO: Setting how present you are

    def update_labels(self, spell_slot: view.SpellSlot):
        self.spell_info_widget.spell_code_label.setText(
            spell_slot.spell.class_code
        )
        self.spell_info_widget.spell_name_label.setText(
            spell_slot.spell.class_name
        )

        self.spell_info_widget.teacher_name_label.setText(
            f"{spell_slot.spell.teacher_name} "
            f"({spell_slot.spell.teacher_code})"
        )

        self.spell_info_widget.time_label.setText(
            f"{spell_slot.start} - {spell_slot.end}"
        )

        self.spell_info_widget.spell_info_widget.spell_slot = spell_slot


class TimetableController:
    def __init__(self, timetable_window: view.TimetableMain,
                 spell_dict: dict, times_dict: dict):
        self.timetable_window = timetable_window
        self.spell_dict = spell_dict
        self.times_dict = times_dict
        self.spell_info_controller = SpellInfoController(
            self.timetable_window.spell_info
        )

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
                spell = model.Spell("Free Spell", "FREE", "", "", "")

            spells[key] = spell

        return spells

    @staticmethod
    def create_day_spells(
            spells: dict[str, model.Spell],
            spell_order: dict[str, list[str]],
            spell_times: dict[str, list[dict[str, list[int, int]]]]
            ) -> dict[str, dict[str, model.SpellSlot]]:
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
            spell_slots = dict()

            # Grab the idx as well to index the spell_times dict correctly
            for idx, spell_id in enumerate(spell_order[day]):
                spell = spells[spell_id]
                times_dict = spell_times[day][idx]

                # Create time objects
                time_start = model.Time(*times_dict["start"])
                time_end = model.Time(*times_dict["end"])

                spell_slots[spell_id] = model.SpellSlot(
                    spell, time_start, time_end, model.AttendanceCode.UNKNOWN
                )

            # Will keep as a string so its easier to work with combobox
            day_spells[day] = spell_slots

        return day_spells

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

    def populate_tabs(self):
        """Adds buttons for all the spells on a day tab"""
        for day in model.Day:
            widget = self.timetable_window.day_widgets[day]
            spell_slots = self.day_spells[str(day).lower()]

            vbox = view.QtWidgets.QVBoxLayout(widget)

            for spell_slot in spell_slots.values():
                button = view.QtWidgets.QPushButton(widget)
                button.setText(
                    f"{spell_slot.spell.class_code}\n" +
                    (
                        # This doesnt show the room if the spell is free
                        # The newline is keep so all have the same height
                        "\n" if spell_slot.spell.class_code == "FREE"
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
        self.timetable_window.show()
        view.app.exec()
