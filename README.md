xorfile
=======

A command-line python utility to generate the bytewise xor result of multiple files.

usage: xorfile.py [-h] [-p PARTS] file [file ...]

Write the result of XORing multiple files to stdout. Divide a single file into
parts by XORing with random data using the -p option.

positional arguments:
* _file_ - files to XOR

optional arguments:
* _-h, --help_  - show this help message and exit
* _-p PARTS, --parts PARTS_  - divide first file into this number of parts; ignore other arguments

