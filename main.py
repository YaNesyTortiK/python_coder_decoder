# Encoder/Decoder by YaNesyTortik
# Created for educational purposes

"""
How to use:
    You must run the program with the following arguments:
    - input file 
        (with extension if you're encoding it  |  If you're decoding, then you don't have to specify extension)
    - output file 
        (without extension if you're encoding it  |  If you're decoding, then you must specify its original extension)
    Or you can specify it after start. (The input rules are the same)

How encoding/decoding work:
    I am generating a binary key (like this one: 1001100).
    Its length is determined by the longest line of data.
    After that I do the following transformations:

    key            -> 10110010
    start string   -> 10010110
    result         -> 00100000

    Explanation: If the symbol in key is 1, then I change the number in the string (below this symbol).
        If 0, then leave as it is.

    Decoding works on the same principle.
    I take the key, which is the first line in the file, and perform the exact same operation, 
    resulting in the original line.
"""

EXTENSION = ".secret"  # You can specify it

import sys
import os
from random import randint
from array import array
from functools import partial


def generate_key(length: int):
    mass = []
    for x in range(length):
        mass.append(randint(0, 1))
    return "".join(str(mass[x]) for x in range(len(mass)))

def encode_char(character: str, key: str):
    encoded = ''
    for i in range(len(key)):
        if key[i] == "1":
            if character[i] == '0':
                encoded += "1"
            else:
                encoded += "0"
        else:
            encoded += character[i]
    return encoded

def decode_char(character: str, key: str):
    decoded = ''
    for i in range(len(key)):
        if key[i] == "1":
            if character[i] == '0':
                decoded += "1"
            else:
                decoded += "0"
        else:
            decoded += character[i]
    return decoded

def to_string(input: list) -> str:
    decoded = []
    for i in input:
        decoded.append(chr(int(i, 2)))
    
    return "".join(decoded)

def generate_file(new_text: list, output_file: str, encoding: bool):
    if encoding:
        output_file += EXTENSION
    basetwo = partial(int, base=2)
    data = array("B", map(basetwo, new_text))
    with open(output_file, "wb") as OUT_FILE:
        data.tofile(OUT_FILE)

def encode_chars(input_file):
    with open(input_file, 'rb') as file:
        text = file.read()

    byte_mass = []

    for i in text:
        byte_mass.append(str(bin(i))[2:])
    
    max_byte_len = 0
    for i in byte_mass:
        if len(i) > max_byte_len:
            max_byte_len = len(i)
    
    key = generate_key(max_byte_len)
    nb_mass = []
    for i in byte_mass:
        n = max_byte_len - len(i)
        nb = "0"*n
        nb_mass.append(f"{nb}{i}")

    new_bytes = [key]
    for i in nb_mass:
        new_bytes.append(encode_char(i, key))
    
    return new_bytes

def decode_chars(input_file: str):
    with open(input_file, 'rb') as file:
        text = file.read()

    byte_mass = []

    for i in text:
        byte_mass.append(str(bin(i))[2:])

    max_byte_len = 0
    for i in byte_mass:
        if len(i) > max_byte_len:
            max_byte_len = len(i)
    nb_mass = []
    for i in byte_mass:
        n = max_byte_len - len(i)
        nb = "0"*n
        nb_mass.append(f"{nb}{i}")

    key = nb_mass[0]
    new_bytes = []
    for i in nb_mass[1:]:
        new_bytes.append(decode_char(i, key))
    
    return new_bytes
    


def encode(input_file: str, output_file: str):
    res = encode_chars(input_file)
    generate_file(res, output_file, True)

def decode(input_file: str, output_file: str = None):
    res = decode_chars(input_file)
    generate_file(res, output_file, False)




if __name__ == "__main__":
    if len (sys.argv) == 1:
        start_file = input("Input file: ")
        end_file = input("Output file: ")
    else:
        if len (sys.argv) < 3:
            raise Warning("You must specify an input file and an output file")

        if len (sys.argv) > 3:
            raise Warning("You can specify ONLY an input file and an output file")
        start_file = sys.argv[1]
        end_file = sys.argv[2]

    add_extension = False
    if not os.path.exists(start_file):
        if not os.path.exists(start_file+EXTENSION):
            raise FileNotFoundError(f'File "{start_file}" Not Found')
        else:
            print("[WARNING] You didn't specify a file extension. The default is decode mode.")
            add_extension = True
        todo = 'd'
    if os.path.exists(end_file):
        print(f'File "{end_file}" Already Exist. Do you want to continue? [y/n]: ', end = "")
        confirm = input()
        if not confirm.lower() == 'y':
            sys.exit(0)
    
    try:
        todo = todo
        print(f'Do you want to start decoding? [y/n]: ', end = "")
        confirm = input()
        if not confirm == 'y':
            sys.exit(0)
    except:
        print("Encode/decode file? [e/d]: ", end = "")
        todo = input()

    if todo.lower()[0] == "e":
        encode(start_file, end_file)
    elif todo.lower()[0] == "d":
        filename, file_extension = os.path.splitext(start_file)
        if add_extension:
            decode(start_file+EXTENSION, end_file)
        else:
            if file_extension == EXTENSION:
                decode(start_file, end_file)
            else:
                raise Warning(f'File extension "{file_extension}" not equals to "{EXTENSION}"')
    else:
        print("Unknown operation.")
        sys.exit(0)
    
    print("Program finished.")
    input("Press Enter to quit: ")
    sys.exit(0)

    