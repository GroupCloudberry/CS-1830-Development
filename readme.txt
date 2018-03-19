BerryDrive Manual

=> Prerequisites
This project is developed around the simplegui framework, using 
simpleguitk to streamline development, as well as introduce additional 
functionality not supported by CodeSkulptor. 

This game can be run natively on any machine with a Python 3 install 
that supports Tkinter, after installing the simpleguitk Python 3 module.

To use all features of this game, simpleguitk *must* be used. 
If not possible, however, fallbacks have been implemented to ensure 
compatibility with CodeSkulptor.

=> Running: simpleguitk (Windows/macOS/Linux)
You need to determine whether the python or python3 command is 
symbolically linked to your Python 3 installation. If python --version 
reports a version number that begins with 2, use python3 in place of python.

To launch the game, simply open a terminal and navigate to the src directory. 
Then run python game.py. The window should appear shortly.

=> Running: simplegui (CodeSkulptor)
In the src directory, there is a subdirectory called cs. Navigate into that 
folder, and findgame.py. Copy the contents of that file into CodeSkulptor, 
and you should be able to run this.

Bear in mind that under CodeSkulptor, certain functionality (e.g. the database) 
will not be present due to its incomplete support for the Python 3 standard library.

=> Player Controls
Some keyboard bindings may not function properly on CodeSkulptor. You can use the 
following tables as a guide for interacting with the game.

==> Menu Navigation
| Action      | simpleguitk              | simplegui (CodeSkulptor) |
|-------------|--------------------------|--------------------------|
| Item up     | Arrow key up             | Arrow key up             |
| Item down   | Arrow key down           | Arrow key up             |
| Select item | Enter or arrow key right | Arrow key right          |

==> Game Controls
| Action        | simpleguitk        | simplegui (CodeSkulptor) |
|---------------|--------------------|--------------------------|
| Pause game    | Esc or click Pause | Letter p or click Pause  |
| Move forward  | Arrow key right    | Arrow key right          |
| Move backward | Arrow key left     | Arrow key left           |

==> Text Input Forms
 Action        | simpleguitk        | simplegui (CodeSkulptor) |
|---------------|--------------------|--------------------------|
| Pause game    | Esc or click Pause | Letter p or click Pause  |
| Move forward  | Arrow key right    | Arrow key right          |
| Move backward | Arrow key left     | Arrow key left           |

=> Worth Mentioning
Some features were not fully implemented due to either technical constraints in 
simplegui, or due to inadequate manpower and time. Nonetheless, the following 
features are accessible to demonstrate.

* Scoreboard - This functionality is fully working in simpleguitk, but not 
simplegui. Nonetheless, the interface for the scoreboard is still accessible 
in the former.
* Player data input form - This is the form used to store player data to the 
SQLite database. Like the scoreboard, it works fully in simpleguitk only but 
is still accessible from both through Save Player in the pause menu (press P 
during gameplay).
* Death screen - The code is functional, but due to bugs, is not loaded in 
gameplay To load it manually, delete 
self.frame.set_draw_handler(self.main_menu.draw_canvas) in game.py and 
replace it with self.frame.set_draw_handler(self.death_menu.draw_canvas).



