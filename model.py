from calendar import MONDAY, THURSDAY, WEDNESDAY
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


class SpellTimes:
    def __init__(self, day, times):
        pass