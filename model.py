from dataclasses import dataclass
from enum import Enum, auto


class AttendanceCode(Enum):
    PRESENT = auto()
    LATE = auto()
    ABSENT = auto()
    MEDICAL = auto()
    CANCELLED = auto()


class Days(Enum):
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


@dataclass
class Spell:
    _class_code: str
    _class_name: str

    # Room is a string because of rooms like T1, T2, gym, etc.
    _class_room: str

    _teacher_code: str
    _teacher_name: str

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
    def __init__(self, day: Days, times, spells):
        pass
