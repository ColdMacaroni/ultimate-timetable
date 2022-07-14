from timetable.model import AttendanceCode

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
