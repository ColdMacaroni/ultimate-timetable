from timetable.model import Day


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

    assert excepted is True, "Didn't raise ValueError with invalid day"


def test_day_from_str_invalid():
    """
    Check that an incorrect key raises an Exception
    """
    day = None

    excepted = False
    try:
        day = Day.from_str("Mokuyoubi")

    except ValueError:
        excepted = True

    assert excepted is True, "Didn't raise ValueError with invalid day"


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
