##
# main.py

from controller import TimetableController
from view import TimetableMain
from sys import argv
import json

def main(json_fn):
    with open(json_fn, 'r') as fp:
        data = json.load(fp)

    win = TimetableMain()
    con = TimetableController(win, data)

    con.run()


if __name__ == "__main__":
    main(argv [1] if len(argv) > 1 else "classes.json")