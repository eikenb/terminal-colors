My goal in writing this script was to provide all the functionality of all the
various perl/sh scripts found around the web in one place with some additional
bells and whistles.

It automatically detects 8, 16, 88, 256 color capabilities (via ncurses) and
displays the appropriate color charts. It can display the colors as blocks or
(2d) cubes optionally with color values overlaid in int or hex values.  It can
show the full rgb text string as well. It can also show the display with a
vertical (default) or horizontal orientation. It has the option of additional
padding and supports -h --help as well.

It also works as a utility for converting between 256 and 88 color values.

In Debian you can install this via... `$ apt-get install colortest-python`
http://packages.debian.org/source/colortest-python
