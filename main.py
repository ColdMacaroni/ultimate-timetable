##
# main.py

from controller import TimetableController
from view import TimetableMain
from sys import argv
import json

def main(spells_fn, times_fn):
    """
    Initializes the controller and the windows, and then starts everything.
    spells_fn: Filename for the JSON with the data for the spells.
    times_fn: Filename for the JSON with the data for the times of each spell.
    """
    # Read the files
    with open(spells_fn, 'r') as fp:
        spell_data = json.load(fp)

    with open(times_fn, 'r') as fp:
            times_data = json.load(fp)

    win = TimetableMain()
    con = TimetableController(win, spell_data, times_data)

    con.run()


if __name__ == "__main__":
    # Using _ before names because this is global by default (thanks python)
    # If we've been provided with an argument
    if len(argv) > 1:
        # In most command line programs - means to read from STDIN
        if argv[1] == '-':
            _spells_fn = input("Spells JSON: ").strip()
        else:
            _spells_fn = argv[1]
    # Go to default value
    else:
        _spells_fn = "spells.json"

    if len(argv) > 2:
        # In most command line programs - means to read from STDIN
        if argv[2] == '-':
            _times_fn = input("Times JSON: ").strip()
        else:
            _times_fn = argv[2]
    # Go to default value
    else:
        _times_fn = "times.json"

    main(_spells_fn, _times_fn)