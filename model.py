from dataclasses import dataclass
from enum import Enum, auto


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
    _class_room: str
    _teacher_code: str
    _teacher_name: str
    _start: tuple[int, int] | list[int, int]
    _end: tuple[int, int] | list[int, int]


class DaySpells:
    def __init__(self, day: Days, times, spells):
        pass
