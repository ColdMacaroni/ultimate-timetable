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
