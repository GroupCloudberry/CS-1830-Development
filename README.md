# BerryDrive
## Prerequisites
This project is developed around the `simplegui` framework, using `simpleguitk` to streamline development, as well as introduce additional functionality not supported by CodeSkulptor. 

This game can be run natively on any machine with a Python 3 install that supports Tkinter, after installing the `simpleguitk` Python 3 module.

To use all features of this game, `simpleguitk` *must* be used. If not possible, however, fallbacks have been implemented to ensure compatibility with CodeSkulptor.
##Running: `simpleguitk` ()
You need to determine whether the `python` or `python3` command is symbolically linked to your Python 3 installation. If `python --version` reports a version number that begins with 2, use `python3` in place of `python`.

To launch the game, simply open a terminal and navigate to the `src` directory. Then run `python game.py`. The window should appear shortly.
##Running: `simplegui` (CodeSkulptor)
In the `src` directory, there is a subdirectory called `cs`. Navigate into that folder, and find`game.py`. Copy the contents of that file into CodeSkulptor, and you should be able to run this.

Bear in mind that under CodeSkulptor, certain functionality (e.g. the database) will not be present due to its incomplete support for the Python 3 standard library.



