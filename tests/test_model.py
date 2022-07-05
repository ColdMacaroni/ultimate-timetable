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


def test_time_minute_setter_upper_boundary_invalid_str():
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


def test_time_minute_setter_upper_boundary_invalid_float():
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
