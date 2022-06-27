import view
import json


class TimetableController:
    def __init__(self, timetable_window: view.TimetableMain):
        self.timetable_window = timetable_window
    
    def run(self):
        self.timetable_window.show()
        view.app.exec()

