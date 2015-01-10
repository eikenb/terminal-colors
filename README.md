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

Help output:
------------

    Usage: colortest-python [options]

    Options:
      -b, --block          Display as block format (vs cube) [default].
      -c, --cube-slice     Display as cube slices (vs block).
      -f, --foreground     Use color for foreground text.
      -l, --rgb            Long format. RGB values as text.
      -n, --numbers        Include color escape numbers on chart.
      -o, --basiccodes     Display 16 color chart with SGR ANSI escape codes.
      -p, --padding        Add extra padding (helps discern colors).
      -v, --vertical       Display with vertical orientation [default].
      -x, --hex            Include hex color numbers on chart.
      -z, --horizontal     Display with horizontal orientation.
      --version            show program's version number and exit
      -h, --help           show this help message and exit

      Conversion options:
        -r N, --256to88=N  Convert (reduce) 256 color value N to an 88 color
                          value.
        -e N, --88to256=N  Convert (expand) 88 color value N to an 256 color
                          value.

Screenshots:
------------
![default](https://github.com/eikenb/terminal-colors/raw/master/screenshots/default.png)
![numbered](https://github.com/eikenb/terminal-colors/raw/master/screenshots/numbers.png)
![long](https://github.com/eikenb/terminal-colors/raw/master/screenshots/long.png)
![padding](https://github.com/eikenb/terminal-colors/raw/master/screenshots/padding.png)
