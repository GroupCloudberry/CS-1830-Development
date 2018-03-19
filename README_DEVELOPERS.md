# CS1830 Development
This repository houses the code for the game.

## Runnning
The source code for this project is written around the `simplegui` module in Python 3 and can be run on the Codeskulptor website. Alternatively, it can also be run on any platform with Tkinter installed.

Using the following block rather than `import simplegui` alone ensures that the `simpleguitk` module will be imported if `simplegui` is absent on the system. This will allow the code to be easily tested during development by running `python filename.py` (or `python3`).

```
try:
    import simplegui
except ImportError:
    import simpleguitk as simplegui
``` 

By installing `simpleguitk` using `pip install simpleguitk` (or `pip3` if `pip --version` reports that Python 2.x is being used), this allows the project code to be run natively (Tkinter required).



