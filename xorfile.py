#!/usr/bin/python

import os
import argparse

RANDOM_FILE = "/dev/urandom"
NAME_PATTERN = "%s.%dof%d.bin"

def xor_files(filenames):
    xor = lambda b1, b2: b1 ^ b2
    files = [open(file, 'rb') for file in filenames]
    result = ""
    while True:
        bytes = [file.read(1) for file in files]
        if "" in bytes:
            break
        result += chr(reduce(xor, [ord(b) for b in bytes]))
    for file in files: 
        file.close()
    return result

def split_file(filename, n):
    filesize = os.path.getsize(filename)
    parts = [NAME_PATTERN % (filename, i, n) for i in range(1, n)]
    with open(RANDOM_FILE, "rb") as random:
        for partname in parts:
            with open(partname, "wb") as part:
                part.write(random.read(filesize))
    with open(NAME_PATTERN % (filename, n, n), "wb") as last_part:
        last_part.write(xor_files([filename] + parts))

def main():
    desc = """Write the result of XORing multiple files to stdout. Divide a 
        single file into parts by XORing with random data using the -p 
        option."""
    phelp = """divide first file into this number of parts; ignore other 
        arguments"""

    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument("-p", "--parts", type=int, help=phelp)
    parser.add_argument('files', metavar='file', nargs='+', help='files to XOR')

    args = parser.parse_args()
    if args.parts:
        split_file(args.files[0], args.parts)
    else:
        print xor_files(args.files),

if __name__ == "__main__":
    main()
