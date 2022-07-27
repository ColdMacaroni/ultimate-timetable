# Timetable
A simple timetable program to manage spells and attendance

## How to run
This program uses python 3.10.

First, make sure you have all the required packages:

`pip3 install -r requirements.txt`

or if pip is not in your path:

`python3 -m pip install -r requirements.txt`

Then, make sure that you have JSON files with spells and the times for each day. The repository includes my
own timetable, but you can use your own or modify them to fit you.

To start it, just run `python3 main.py` from the root folder. This will automatically read the `spells.json`
and `times.json` files.

You can also specify your own JSON files with `python3 main.py spells_filename.json times_filename.json`.

### Running tests
The tests use the pytest framework. I've had trouble getting VSCodium to recognise my tests, but you can just as
easily run `pytest tests` from the root folder.
