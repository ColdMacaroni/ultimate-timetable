from timetable.model import (
    Day,
    Spell,
    Time,
    SpellSlot,
    DaySpells,
    AttendanceCode
)


def create_dayspell() -> tuple[DaySpells, Day, list[SpellSlot]]:
    """
    Creates a DaySpells object with test attributes.
    This function is used for consistency and because a DaySpell object is
    quite verbose to create.
    """
    DAY = Day.MONDAY

    ATTENDANCE = AttendanceCode.PRESENT

    SPELLSLOTS = [
        SpellSlot(
            Spell(
                "Class Name 1",
                "NAME1",
                "1",
                "Teacher name 1",
                "NTE1"
            ),
            Time(1, 00),
            Time(1, 45),
            ATTENDANCE
        ),
        SpellSlot(
            Spell(
                "Class Name 2",
                "NAME2",
                "2",
                "Teacher name 2",
                "NTE2"
            ),
            Time(2, 00),
            Time(2, 45),
            ATTENDANCE
        ),
        SpellSlot(
            Spell(
                "Class Name 3",
                "NAME3",
                "3",
                "Teacher name 3",
                "NTE3"
            ),
            Time(3, 00),
            Time(3, 45),
            ATTENDANCE
        ),
        SpellSlot(
            Spell(
                "Class Name 4",
                "NAME4",
                "4",
                "Teacher name 4",
                "NTE4"
            ),
            Time(4, 00),
            Time(4, 45),
            ATTENDANCE
        ),
        SpellSlot(
            Spell(
                "Class Name 5",
                "NAME5",
                "5",
                "Teacher name 5",
                "NTE5"
            ),
            Time(5, 00),
            Time(5, 45),
            ATTENDANCE
        ),
    ]

    return DaySpells(DAY, SPELLSLOTS), DAY, SPELLSLOTS


def test_init():
    """
    Checks that the created spell has the same objects and values as it was
    given
    """
    dayspell, day, spellslots = create_dayspell()

    assert spellslots is dayspell.spell_slots,\
        "Given SpellSlot list and list in DaySpells object are different."

    assert day is dayspell.day,\
        "Given Day enum and Day in DaySpells object are different."


def test_spell_five_true():
    """
    Checks that the spell_five member is True by default
    """
    dayspell, day, spellslots = create_dayspell()

    assert dayspell.spell_five is True,\
        "DaySpells object's spell five should be True by default."


def test_spell():
    """
    Checks that the spell method returns the correct object
    """
    dayspell, day, spellslots = create_dayspell()

    for idx, slot in enumerate(spellslots):
        assert dayspell.spell(idx) is slot,\
            "spell method of DaySpells object returns a different object "\
            f"at index {idx}"


def test_time():
    """
    Checks that the time method returns the correct tuple
    """
    dayspell, day, spellslots = create_dayspell()

    for idx, slot in enumerate(spellslots):
        assert dayspell.times(idx) == (slot.start, slot.end),\
            "time method of DaySpells object returns different times "\
            f"at index {idx}"


# Setters
def test_spell_five_setter_valid():
    """
    Check that spell_five can be set correctly to a valid value
    """
    dayspell, day, spellslots = create_dayspell()

    TO_SET = False

    exception_raised = False
    try:
        dayspell.spell_five = TO_SET

    except ValueError:
        exception_raised = True

    assert exception_raised is False,\
        "Exception raised when setting spell_five to a valid value"

    assert dayspell.spell_five == TO_SET,\
        "spell_five not set to value despite no exceptions raised"


def test_spell_five_setter_invalid():
    """
    Check that spell_five cant be set to an invalid value
    """
    dayspell, day, spellslots = create_dayspell()

    TO_SET = "No spell five, sorry."

    exception_raised = False
    try:
        dayspell.spell_five = TO_SET

    except ValueError:
        exception_raised = True

    assert exception_raised is True,\
        "ValueError not raised when setting spell_five to an invalid value"

    assert dayspell.spell_five != TO_SET,\
        "spell_five is set to value despite ValueError raised"


def test_day_setter_valid():
    """
    Check that day can be set correctly to a valid value
    """
    dayspell, day, spellslots = create_dayspell()

    TO_SET = Day.THURSDAY

    exception_raised = False
    try:
        dayspell.day = TO_SET

    except ValueError:
        exception_raised = True

    assert exception_raised is False,\
        "Exception raised when setting day to a valid value"

    assert dayspell.day is TO_SET,\
        "day not set to value despite no exceptions raised"


def test_day_setter_invalid():
    """
    Check that day cant be set to an invalid value
    """
    dayspell, day, spellslots = create_dayspell()

    TO_SET = "Nope."

    exception_raised = False
    try:
        dayspell.day = TO_SET

    except ValueError:
        exception_raised = True

    assert exception_raised is True,\
        "ValueError not raised when setting day to an invalid value"

    assert dayspell.day != TO_SET,\
        "day is set to value despite ValueError raised"


def test_spell_slots_setter_valid():
    """
    Check that spell_slots can be set correctly to a valid value
    """
    dayspell, day, spellslots = create_dayspell()

    TO_SET = [SpellSlot(
        Spell("Class Name 1", "NAME1", "1", "Teacher name 1", "NTE1"),
        Time(1, 00),
        Time(1, 45), AttendanceCode.LATE)]

    exception_raised = False
    try:
        dayspell.spell_slots = TO_SET

    except ValueError:
        exception_raised = True

    assert exception_raised is False,\
        "Exception raised when setting spell_slots to a valid value"

    assert dayspell.spell_slots == TO_SET,\
        "spell_slots not set to value despite no exceptions raised"


def test_spell_slots_setter_boundary_valid_empty():
    """
    Check that spell_slots can be set correctly to an empty list
    """
    dayspell, day, spellslots = create_dayspell()

    TO_SET = []

    exception_raised = False
    try:
        dayspell.spell_slots = TO_SET

    except ValueError:
        exception_raised = True

    assert exception_raised is False,\
        "Exception raised when setting spell_slots to a valid value"

    assert dayspell.spell_slots == TO_SET,\
        "spell_slots not set to value despite no exceptions raised"


def test_spell_slots_setter_invalid():
    """
    Check that spell_slots cant be set to an invalid value
    """
    dayspell, day, spellslots = create_dayspell()

    TO_SET = "No spell five, sorry."

    exception_raised = False
    try:
        dayspell.spell_slots = TO_SET

    except ValueError:
        exception_raised = True

    assert exception_raised is True,\
        "ValueError not raised when setting spell_slots to an invalid value"

    assert dayspell.spell_slots != TO_SET,\
        "spell_slots is set to value despite ValueError raised"


def test_spell_slots_setter_boundary_invalid_list_type():
    """
    Check that spell_slots can't be set to a list with the wrong types
    """
    dayspell, day, spellslots = create_dayspell()

    TO_SET = ["Hmmm", "Strange", SpellSlot(
        Spell("Class Name 1", "NAME1", "1", "Teacher name 1", "NTE1"),
        Time(1, 00),
        Time(1, 45), AttendanceCode.LATE)
    ]

    exception_raised = False
    try:
        dayspell.spell_slots = TO_SET

    except ValueError:
        exception_raised = True

    assert exception_raised is True,\
        "ValueError not raised when setting spell_slots to an invalid value"

    assert dayspell.spell_slots != TO_SET,\
        "spell_slots is set to value despite ValueError raised"
