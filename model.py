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
    _hour: int
    _minute: int

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
        match self:
            case self.MONDAY:
                return "Monday"
            case self.TUESDAY:
                return "Tuesday"
            case self.WEDNESDAY:
                return "Wednesday"
            case self.THURSDAY:
                return "Thursday"
            case self.FRIDAY:
                return "Friday"
            case _:
                self


@dataclass
class Spell:
    _class_name: str
    _class_code: str

    # Room is a string because of rooms like T1, T2, gym, etc.
    _class_room: str

    _teacher_code: str
    _teacher_name: str

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

    @class_code.setter
    def class_code(self, new) -> str:
        if not isinstance(new, str):
            raise ValueError("Class code must be a string")

        self._class_code = new

    @property
    def teacher_code(self) -> str:
        return self._teacher_code

    @teacher_code.setter
    def teacher_code(self, new) -> str:
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


class DaySpells:
    def __init__(self, day: Day, times, spells: list[Spell]):
        pass
