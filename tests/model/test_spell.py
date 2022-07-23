from timetable.model import Spell


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
