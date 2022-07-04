import view
import model
import json


class SpellInfoController:
    def __init__(self, spell_info_widget: view.SpellInfoWidget):
        self.spell_info_widget = spell_info_widget

    def update_labels(self, spell_slot: view.SpellSlot):
        self.spell_code_label.setText(spell_slot.spell.class_code)
        self.spell_name_label.setText(spell_slot.spell.class_name)

        self.teacher_name_label.setText(f"{spell_slot.spell.teacher_name} ({spell_slot.spell.teacher_code})")
        
        self.time_label.setText(f"{spell_slot.start} - {spell_slot.end}")


class TimetableController:
    def __init__(self, timetable_window: view.TimetableMain,
                 spell_dict: dict, times_dict: dict):
        self.timetable_window = timetable_window
        self.spell_dict = spell_dict
        self.times_dict = times_dict

        self.spells = self.create_spells(self.spell_dict["spells"])

        self.day_spells = self.create_day_spells(
            self.spells,
            self.spell_dict["days"],
            self.times_dict
        )

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
            ) -> dict[str, model.SpellSlot]:
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
                    spell, time_start, time_end
                )

            # Will keep as a string so its easier to work with combobox
            day_spells[day] = spell_slots

        return day_spells
    
    def populate_tabs(self):
        for day in model.Day:
            widget = self.timetable_window.day_widgets[day]
            spells = self.day_spells

    def run(self):
        self.timetable_window.show()
        view.app.exec()
