from dataclasses import dataclass
from enum import Enum, auto


class AttendanceCode(Enum):
    PRESENT = auto()
    LATE = auto()
    ABSENT = auto()
    MEDICAL = auto()
    CANCELLED = auto()

    def __str__(self):
        reversed_dict = dict(map(reversed, self.str_dict.items()))

        return reversed_dict[self]

    @classmethod
    def from_str(cls, s: str) -> "AttendanceCode":
        if s not in cls.str_dict:
            raise ValueError(f"{s} is not an appropriate attendance code")

        return cls.str_dict[s]

    @classmethod
    @property
    def str_dict(self):
        str_to_attr = {
            "P": self.PRESENT,
            "L": self.LATE,
            "?": self.ABSENT,
            "M": self.MEDICAL,
            "F": self.CANCELLED
        }

        return str_to_attr


@dataclass
class Time:
    hour: int
    minute: int

    MINUTES = 60
    HOURS = 24

    def __str__(self):
        return f"{self.hour:02}:{self.minute:02}"

    @property
    def hour(self):
        return self._hour

    @hour.setter
    def hour(self, new):
        if new < 0 or new >= self.HOURS:
            raise ValueError("Invalid hour")

        self._hour = new

    @property
    def minute(self):
        return self._minute

    @minute.setter
    def minute(self, new):
        if new < 0 or new >= self.MINUTES:
            raise ValueError("Invalid minute")

        self._minute = new


class Day(Enum):
    MONDAY = auto()
    TUESDAY = auto()
    WEDNESDAY = auto()
    THURSDAY = auto()
    FRIDAY = auto()

    def __str__(self):
        reversed_dict = dict(map(reversed, self.str_dict.items()))

        # Capitalize so it looks pretty :^)
        return reversed_dict[self].capitalize()

    @classmethod
    def from_str(cls, s: str) -> "Day":
        if s not in cls.str_dict:
            raise ValueError(f"{s} is not a valid day")

        return cls.str_dict[s]

    @classmethod
    @property
    def str_dict(cls):
        # These aren't capitalized so its easier to do stuff with
        str_to_attr = {
                "monday": cls.MONDAY,
                "tuesday": cls.TUESDAY,
                "wednesday": cls.WEDNESDAY,
                "thursday": cls.THURSDAY,
                "friday": cls.FRIDAY
        }

        return str_to_attr


@dataclass
class Spell:
    class_name: str
    class_code: str

    # Room is a string because of rooms like T1, T2, gym, etc.
    class_room: str

    teacher_code: str
    teacher_name: str

    @classmethod
    def from_dict(cls, d: dict[str, str]):
        return cls(d["name"],
                   d["code"],
                   d["room"],
                   d["teacher_code"],
                   d["teacher_name"])

    @property
    def class_code(self) -> str:
        return self._class_code

    @class_code.setter
    def class_code(self, new) -> str:
        if not isinstance(new, str):
            raise ValueError("Class code must be a string")

        self._class_code = new

    @property
    def class_name(self) -> str:
        return self._class_name

    @class_name.setter
    def class_name(self, new) -> str:
        if not isinstance(new, str):
            raise ValueError("Class name must be a string")

        self._class_name = new

    @property
    def class_room(self) -> str:
        return self._class_room

    @class_room.setter
    def class_room(self, new) -> str:
        if not isinstance(new, str):
            raise ValueError("Class room must be a string")

        self._class_room = new

    @property
    def teacher_code(self) -> str:
        return self._teacher_code

    @teacher_code.setter
    def teacher_code(self, new) -> str:
        # I'm tempted to check that it can only be 3 chars, but I won't
        # because I'm not 100% sure of the format.
        if not isinstance(new, str):
            raise ValueError("Teacher code must be a string")

        self._teacher_code = new

    @property
    def teacher_name(self) -> str:
        return self._teacher_name

    @teacher_name.setter
    def teacher_name(self, new) -> str:
        if not isinstance(new, str):
            raise ValueError("Teacher name must be a string")

        self._teacher_name = new


@dataclass
class SpellSlot:
    spell: Spell
    start: Time
    end: Time
    # TODO: attr for being present

    @property
    def spell(self) -> Spell:
        return self._spell

    @spell.setter
    def spell(self, new):
        if not isinstance(new, Spell):
            raise ValueError("New spell is not of type Spell")

        self._spell = new

    @property
    def start(self) -> Time:
        return self._start

    @start.setter
    def start(self, new):
        if not isinstance(new, Time):
            raise ValueError("New start ime is not of type Time")

        self._start = new

    @property
    def end(self) -> Time:
        return self._end

    @end.setter
    def end(self, new):
        if not isinstance(new, Time):
            raise ValueError("New end time is not of type Time")

        self._end = new


class DaySpells:
    _spell_five = True

    def __init__(self, day: Day, spell_slots: dict[str, SpellSlot]):
        self.day = day
        self.spell_slots = spell_slots

    def spell(self, spell_str: str) -> Spell:
        """
        Returns the spell object of the slot pointed by the str.
        The str being either a number or "ako"
        """
        return self.spell_slots[spell_str].spell

    def times(self, spell_str) -> tuple[Time, Time]:
        """
        Returns the start and end Time objects of the slot pointed by the str.
        The str being either a number or "ako"
        """
        spell_slot = self.spell_slots[spell_str]
        return spell_slot.start, spell_slot.end

    @property
    @classmethod
    def spell_five(cls) -> bool:
        return cls._spell_five

    @spell_five.setter
    @classmethod
    def spell_five(cls, new):
        if not isinstance(cls, bool):
            raise ValueError("Spell 5 must be a boolean")
        cls._spell_five = new

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, new):
        if new not in Day:
            raise ValueError("Value is not of Day enum")

        self._day = new

    @property
    def spell_slots(self):
        return self._spell_slots

    @spell_slots.setter
    def spell_slots(self, new):
        # All must be spellslot
        if not all(map(lambda x: isinstance(x, SpellSlot), new)):
            raise ValueError("New spell slots list must only"
                             "have SpellSlot dataclass")

        self._spell_slots = new
