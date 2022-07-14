from timetable.model import SpellSlot, Spell, Time, AttendanceCode


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
