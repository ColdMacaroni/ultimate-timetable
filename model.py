from calendar import MONDAY, THURSDAY, WEDNESDAY
from dataclasses import dataclass
from enum import Enum, auto

class Days(Enum): 
    MONDAY = auto()
    TUESDAY = auto()
    WEDNESDAY = auto()
    THURSDAY = auto()
    FRIDAY = auto()

    @classmethod
    def str(cls, day):
        match day:
            case cls.MONDAY:
                return "monday"
            case cls.TUESDAY:
                return "tuesday"
            case cls.WEDNESDAY:
                return "wednesday"
            case cls.THURSDAY:
                return "thursday"
            case cls.FRIDAY:
                return "friday"


class SpellTimes:
    def __init__(self, day, times)