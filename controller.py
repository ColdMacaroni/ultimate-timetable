import view
import model
import json


class TimetableController:
    def __init__(self, timetable_window: view.TimetableMain,
                 spell_dict: dict, times_dict: dict):
        self.timetable_window = timetable_window
        self.spell_dict = spell_dict
        self.times_dict = times_dict

        self.spells = self.create_spells(self.spell_dict["spells"])
        
        #TODO:::::::
        self.day_spells = self.create_day_spell(self.spells, self.spells["days"])
        # TODO: Create spellslot object for each spell
        # TODO: Create DaySpells classes for each day

    @staticmethod
    def create_spells(spells_dict) -> dict[str, model.Spell]:
        spells = dict()

        for key, val in spells_dict.items():
            if val is not None:
                spell = model.Spell(**val)

            # Nones are free spells, they are None and not just another spell
            # because two types(keys) of spells can be free.
            else:
                spell = model.Spell("Free Spell", "FREE", "", "", "")

            spells[key] = spell

        return spells

    def run(self):
        self.timetable_window.show()
        view.app.exec()
