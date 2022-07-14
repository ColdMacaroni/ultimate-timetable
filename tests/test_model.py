from timetable.model import *


def test_attendance_from_str():
    """
    Checks that you get the correct attribute from a string
    """
    assert AttendanceCode.from_str("P") == AttendanceCode.PRESENT,\
        "Invalid AttendanceCode from string"

    assert AttendanceCode.from_str("L") == AttendanceCode.LATE,\
        "Invalid AttendanceCode from string"

    assert AttendanceCode.from_str("?") == AttendanceCode.ABSENT,\
        "Invalid AttendanceCode from string"

    assert AttendanceCode.from_str("M") == AttendanceCode.MEDICAL,\
        "Invalid AttendanceCode from string"

    assert AttendanceCode.from_str("F") == AttendanceCode.CANCELLED,\
        "Invalid AttendanceCode from string"

    assert AttendanceCode.from_str("") == AttendanceCode.UNKNOWN,\
        "Invalid AttendanceCode from string"


def test_attendance_str():
    """
    Checks that attendance codes are cast to the correct string
    """
    assert str(AttendanceCode.PRESENT) == "P",\
        "Wrong string from attendance code"

    assert str(AttendanceCode.LATE) == "L",\
        "Wrong string from attendance code"

    assert str(AttendanceCode.ABSENT) == "?",\
        "Wrong string from attendance code"

    assert str(AttendanceCode.MEDICAL) == "M",\
        "Wrong string from attendance code"

    assert str(AttendanceCode.CANCELLED) == "F",\
        "Wrong string from attendance code"

    assert str(AttendanceCode.UNKNOWN) == "",\
        "Wrong string from attendance code"


def test_time_str():
    """
    Checks that the time is correctly converted to a string
    """
    t = Time(7, 5)

    assert str(t) == "07:05", "Incorrect string from Time object"


def test_time_hour_setter_valid():
    """
    Check that time dataclass accepts a normal hour
    """
    t = Time(2, 0)

    excepted = False
    TO_SET = 11
    try:
        t.hour = TO_SET

    except ValueError:
        excepted = True

    assert excepted is False, "Raised value error on valid 24hr time"
    assert t.hour == TO_SET, "Value wasn't set"


def test_time_hour_setter_upper_boundary_valid():
    """
    Check that time dataclass accepts a normal hour at the upper boundary
    """
    t = Time(2, 0)

    excepted = False
    TO_SET = 23
    try:
        t.hour = TO_SET

    except ValueError:
        excepted = True

    assert excepted is False, "Raised value error on valid 24hr time"
    assert t.hour == TO_SET, "Value wasn't set"


def test_time_hour_setter_lower_boundary_valid():
    """
    Check that time dataclass accepts a normal hour at the lower boundary
    """
    t = Time(2, 0)

    excepted = False
    TO_SET = 0
    try:
        t.hour = TO_SET

    except ValueError:
        excepted = True

    assert excepted is False, "Raised value error on valid 24hr time"
    assert t.hour == TO_SET, "Value wasn't set"


def test_time_hour_setter_lower_boundary_invalid():
    """
    Check that time dataclass doesnt accept an hour below the lower boundary
    """
    t = Time(2, 0)

    excepted = False
    TO_SET = -1
    try:
        t.hour = TO_SET

    except ValueError:
        excepted = True

    assert excepted is True, "Didn't raise value error on invalid 24hr time"
    assert t.hour != TO_SET, "Value was set despite being invalid"


def test_time_hour_setter_upper_boundary_invalid():
    """
    Check that time dataclass doesnt accept an hour above the upper boundary
    """
    t = Time(2, 0)

    excepted = False
    # 24hr time goes 0-23
    TO_SET = 24
    try:
        t.hour = TO_SET

    except ValueError:
        excepted = True

    assert excepted is True, "Didn't raise value error on invalid 24hr time"
    assert t.hour != TO_SET, "Value was set despite being invalid"


def test_time_hour_setter_upper_boundary_invalid_str():
    """
    Check that time dataclass doesnt accept an invalid type as hour
    """
    t = Time(2, 0)

    excepted = False

    TO_SET = "Horse"
    try:
        t.hour = TO_SET

    except ValueError:
        excepted = True

    assert excepted is True, "Didn't raise value error on invalid 24hr time"
    assert t.hour != TO_SET, "Value was set despite being invalid"


def test_time_hour_setter_upper_boundary_invalid_float():
    """
    Check that time dataclass doesnt accept an invalid type as hour
    """
    t = Time(2, 0)

    excepted = False

    TO_SET = 3.4
    try:
        t.hour = TO_SET

    except ValueError:
        excepted = True

    assert excepted is True, "Didn't raise value error on invalid 24hr time"
    assert t.hour != TO_SET, "Value was set despite being invalid"


def test_time_minute_setter_valid():
    """
    Check that time dataclass accepts a normal minute
    """
    t = Time(2, 0)

    excepted = False
    TO_SET = 30
    try:
        t.minute = TO_SET

    except ValueError:
        excepted = True

    assert excepted is False, "Raised value error on valid minute"
    assert t.minute == TO_SET, "Value wasn't set"


def test_time_minute_setter_upper_boundary_valid():
    """
    Check that time dataclass accepts a normal minute at the upper boundary
    """
    t = Time(2, 0)

    excepted = False
    TO_SET = 59
    try:
        t.minute = TO_SET

    except ValueError:
        excepted = True

    assert excepted is False, "Raised value error on valid minute"
    assert t.minute == TO_SET, "Value wasn't set"


def test_time_minute_setter_lower_boundary_valid():
    """
    Check that time dataclass accepts a normal minute at the lower boundary
    """
    t = Time(2, 3)

    excepted = False
    TO_SET = 0
    try:
        t.minute = TO_SET

    except ValueError:
        excepted = True

    assert excepted is False, "Raised value error on valid minute"
    assert t.minute == TO_SET, "Value wasn't set"


def test_time_minute_setter_lower_boundary_invalid():
    """
    Check that time dataclass doesnt accept a minute below the lower boundary
    """
    t = Time(2, 0)

    excepted = False
    TO_SET = -1
    try:
        t.minute = TO_SET

    except ValueError:
        excepted = True

    assert excepted is True, "Didn't raise value error on invalid minute"
    assert t.minute != TO_SET, "Value was set despite being invalid"


def test_time_minute_setter_upper_boundary_invalid():
    """
    Check that time dataclass doesnt accept a minute above the upper boundary
    """
    t = Time(2, 0)

    excepted = False

    # minutes should go from 0-59
    TO_SET = 60
    try:
        t.minute = TO_SET

    except ValueError:
        excepted = True

    assert excepted is True, "Didn't raise value error on invalid minute"
    assert t.minute != TO_SET, "Value was set despite being invalid"


def test_time_minute_setter_invalid_str():
    """
    Check that time dataclass doesnt accept an invalid type as minute
    """
    t = Time(2, 0)

    excepted = False

    TO_SET = "Horse"
    try:
        t.minute = TO_SET

    except ValueError:
        excepted = True

    assert excepted is True, "Didn't raise value error on invalid minute"
    assert t.minute != TO_SET, "Value was set despite being invalid"


def test_time_minute_setter_invalid_float():
    """
    Check that time dataclass doesnt accept an invalid type as minute
    """
    t = Time(2, 0)

    excepted = False

    TO_SET = 3.4
    try:
        t.minute = TO_SET

    except ValueError:
        excepted = True

    assert excepted is True, "Didn't raise value error on invalid minute"
    assert t.minute != TO_SET, "Value was set despite being invalid"


#######
# Day #
#######

##
# Valid
def test_day_from_str():
    """
    Check that the correct attribute is returned from a string
    """
    assert Day.from_str("monday") == Day.MONDAY,\
        "Wrong day attribute returned from string"

    assert Day.from_str("tuesday") == Day.TUESDAY,\
        "Wrong day attribute returned from string"

    assert Day.from_str("wednesday") == Day.WEDNESDAY,\
        "Wrong day attribute returned from string"

    assert Day.from_str("thursday") == Day.THURSDAY,\
        "Wrong day attribute returned from string"

    assert Day.from_str("friday") == Day.FRIDAY,\
        "Wrong day attribute returned from string"


def test_day_from_str_boundary_invalid():
    """
    Check that different case doesnt return an attribute
    Will assume that this is the same for all the atttributes
    """
    day = None

    excepted = False
    try:
        day = Day.from_str("MonDAY")

    except ValueError:
        excepted = True

    assert excepted is True, "Didn't raise KeyError with invalid day"


def test_day_str():
    """
    Check that the attributes get turned into the correct string
    """
    assert str(Day.MONDAY) == "Monday",\
        "Wrong string returned from day attribute"

    assert str(Day.TUESDAY) == "Tuesday",\
        "Wrong string returned from day attribute"

    assert str(Day.WEDNESDAY) == "Wednesday",\
        "Wrong string returned from day attribute"

    assert str(Day.THURSDAY) == "Thursday",\
        "Wrong string returned from day attribute"

    assert str(Day.FRIDAY) == "Friday",\
        "Wrong string returned from day attribute"


#########
# Spell #
#########

##
# Valid
def test_spell_from_dict():
    spell_dict = {
        "name": "Spell name",
        "code": "SPN",
        "room": "45H",
        "teacher_code": "NOT",
        "teacher_name": "No Teacher"
    }

    spell = Spell(
        spell_dict["name"],
        spell_dict["code"],
        spell_dict["room"],
        spell_dict["teacher_code"],
        spell_dict["teacher_name"],
    )

    assert spell.class_name == spell_dict["name"],\
        "Spell name not set correctly"

    assert spell.class_code == spell_dict["code"],\
        "Spell code not set correctly"

    assert spell.class_room == spell_dict["room"],\
        "Spell room not set correctly"

    assert spell.teacher_name == spell_dict["teacher_name"],\
        "Teacher name not set correctly"

    assert spell.teacher_code == spell_dict["teacher_code"],\
        "Teacher code not set correctly"


def test_spell_class_name_setter_valid():
    """
    Check that the class_name attr can be changed
    """
    spell = Spell("Cool name", "CODE", "2", "TEA", "Teacher Name")

    TO_SET = "Banaba"

    excepted = False
    try:
        spell.class_name = TO_SET

    except ValueError:
        excepted = True

    assert excepted is False,\
        "ValueError raised when setting a valid spell name"
    assert spell.class_name == TO_SET, "Spell name not set"


def test_spell_class_code_setter_valid():
    """
    Check that the class_code attr can be changed
    There is no set format for class code.
    """
    spell = Spell("Cool name", "CODE", "2", "TEA", "Teacher Name")

    TO_SET = "BAN"

    excepted = False
    try:
        spell.class_code = TO_SET

    except ValueError:
        excepted = True

    assert excepted is False,\
        "ValueError raised when setting a valid spell code"
    assert spell.class_code == TO_SET, "Spell code not set"


def test_spell_class_room_setter_valid():
    """
    Check that the class_room attr can be changed
    """
    spell = Spell("Cool name", "CODE", "2", "TEA", "Teacher Name")

    TO_SET = "10T"

    excepted = False
    try:
        spell.class_room = TO_SET

    except ValueError:
        excepted = True

    assert excepted is False,\
        "ValueError raised when setting a valid spell room"
    assert spell.class_room == TO_SET, "Spell room not set"


def test_spell_teacher_name_setter_valid():
    """
    Check that the teacher_name attr can be changed
    """
    spell = Spell("Cool name", "CODE", "2", "TEA", "Teacher Name")

    TO_SET = "Mr Cool Teach"

    excepted = False
    try:
        spell.teacher_name = TO_SET

    except ValueError:
        excepted = True

    assert excepted is False,\
        "ValueError raised when setting a valid teacher name"
    assert spell.teacher_name == TO_SET, "Teacher code not set"


def test_spell_teacher_code_setter_valid():
    """
    Check that the teacher_code attr can be changed
    There is no set format for teacher code.
    """
    spell = Spell("Cool name", "CODE", "2", "TEA", "Teacher Name")

    TO_SET = "NCO"

    excepted = False
    try:
        spell.teacher_code = TO_SET

    except ValueError:
        excepted = True

    assert excepted is False,\
        "ValueError raised when setting a valid teacher code"
    assert spell.teacher_code == TO_SET, "Teacher code not set"


##
# Invalid
def test_spell_class_name_setter_invalid_type():
    """
    Check that the class_name attr cant be set to wrong type
    """
    spell = Spell("Cool name", "CODE", "2", "TEA", "Teacher Name")

    TO_SET = 1337

    excepted = False
    try:
        spell.class_name = TO_SET

    except ValueError:
        excepted = True

    assert excepted is True,\
        "ValueError not raised when setting an invalid spell name"
    assert spell.class_name != TO_SET, "Spell name set despite being invalid"


def test_spell_class_name_setter_boundary_invalid_empty():
    """
    Check that the class_name attr cant be set to an empty string
    Well assume that everything but class name and class code can be empty
    """
    spell = Spell("Cool name", "CODE", "2", "TEA", "Teacher Name")

    TO_SET = ""

    excepted = False
    try:
        spell.class_name = TO_SET

    except ValueError:
        excepted = True

    assert excepted is True,\
        "ValueError not raised when setting an invalid spell name"
    assert spell.class_name != TO_SET, "Spell name set despite being invalid"


def test_spell_class_code_setter_boundary_invalid_empty():
    """
    Check that the class_code attr cant be set to empty string
    """
    spell = Spell("Cool name", "CODE", "2", "TEA", "Teacher Name")

    TO_SET = ""

    excepted = False
    try:
        spell.class_code = TO_SET

    except ValueError:
        excepted = True

    assert excepted is True,\
        "ValueError not raised when setting an invalid spell code"
    assert spell.class_code != TO_SET, "Spell code set despite being invalid"


def test_spell_class_code_setter_invalid_type():
    """
    Check that the class_code attr cant be set to incorrect type
    """
    spell = Spell("Cool name", "CODE", "2", "TEA", "Teacher Name")

    TO_SET = 120

    excepted = False
    try:
        spell.class_code = TO_SET

    except ValueError:
        excepted = True

    assert excepted is True,\
        "ValueError not raised when setting an invalid spell code"
    assert spell.class_code != TO_SET, "Spell code set despite being invalid"


def test_spell_class_room_setter_invalid_type():
    """
    Check that the class_room attr cant be set to a wrong type
    We'll accept empty strings because of free spells
    """
    spell = Spell("Cool name", "CODE", "2", "TEA", "Teacher Name")

    TO_SET = 34

    excepted = False
    try:
        spell.class_room = TO_SET

    except ValueError:
        excepted = True

    assert excepted is True,\
        "ValueError not raised when setting an invalid spell room"
    assert spell.class_room != TO_SET, "Spell room set despite being invalid"


def test_spell_teacher_name_setter_invalid():
    """
    Check that the teacher_name attr cant be set to an invalid type
    """
    spell = Spell("Cool name", "CODE", "2", "TEA", "Teacher Name")

    TO_SET = ["Epic", "Teacher"]

    excepted = False
    try:
        spell.teacher_name = TO_SET

    except ValueError:
        excepted = True

    assert excepted is True,\
        "ValueError not raised when setting an invalid teacher name"
    assert spell.teacher_name != TO_SET,\
        "Teacher code set despite being invalid"


def test_spell_teacher_code_setter_invalid():
    """
    Check that the teacher_code attr can't be set to an invalid type
    There is no set format for teacher code. Only has to be str
    """
    spell = Spell("Cool name", "CODE", "2", "TEA", "Teacher Name")

    TO_SET = 0

    excepted = False
    try:
        spell.teacher_code = TO_SET

    except ValueError:
        excepted = True

    assert excepted is True,\
        "ValueError not raised when setting an invalid teacher code"

    assert spell.teacher_code != TO_SET,\
        "Teacher code set despite being invalid"


##############
# Spell Slot #
##############

##
# Valid
def test_spellslot_valid():
    """
    Checks that the SpellSlot is created correctly, with all its attributes set
    and stuff
    """
    # These are constants so we can be sure the objects arent modified when put
    # into the spell slot

    # Spell
    SPELL_NAME = "Spell Name"
    SPELL_CODE = "CODE"
    SPELL_ROOM = "1"
    SPELL_TEACHER_CODE = "TEA"
    SPELL_TEACHER_NAME = "Teacher Name"

    spell = Spell(
        SPELL_NAME,
        SPELL_CODE,
        SPELL_ROOM,
        SPELL_TEACHER_CODE,
        SPELL_TEACHER_NAME
    )

    # Start
    START_HOUR = 4
    START_MINUTE = 34

    start = Time(START_HOUR, START_MINUTE)

    # End
    END_HOUR = 5
    END_MINUTE = 54
    end = Time(END_HOUR, END_MINUTE)

    ATTENDANCE_CODE = AttendanceCode.PRESENT

    spell_slot = SpellSlot(spell, start, end, ATTENDANCE_CODE)

    # Check spell related stuff
    assert spell_slot.spell is spell,\
        "spell attribute set to a different object"

    assert spell_slot.spell.class_name == SPELL_NAME,\
        "Spell name changed"

    assert spell_slot.spell.class_code == SPELL_CODE,\
        "Spell code changed"

    assert spell_slot.spell.class_room == SPELL_ROOM,\
        "Spell room changed"

    assert spell_slot.spell.teacher_code == SPELL_TEACHER_CODE,\
        "Spell teacher name changed"

    assert spell_slot.spell.teacher_name == SPELL_TEACHER_NAME,\
        "Spell teacher code changed"

    # Check time related stuff
    assert spell_slot.start is start,\
        "Start time object is different"

    assert spell_slot.start.hour == START_HOUR,\
        "Start hour is different"

    assert spell_slot.start.minute == START_MINUTE,\
        "Start minute is different"

    assert spell_slot.end is end,\
        "End time object is different"

    assert spell_slot.end.hour == END_HOUR,\
        "End hour is different"

    assert spell_slot.end.minute == END_MINUTE,\
        "End minute is different"

    # Attendance
    assert spell_slot.attendance is ATTENDANCE_CODE,\
        "Attendance code set to a different object"


def test_spellslot_spell_setter():
    spell = Spell("Spell name", "CODE", "23", "TEA", "Teacher Name")
    start = Time(1, 14)
    end = Time(2, 5)
