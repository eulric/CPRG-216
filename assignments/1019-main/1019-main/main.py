"""
Unit 5 - Lab 2
Personal repo on GitHub
"""

import string
import random

charList = string.printable
POS = random.randint(1, len(charList))


def cipher(line):
    """offset a character of a line based on its position in the charList"""
    out = ""

    for char in line:
        ind = charList.index(char)
        off_set = ind + POS
        if off_set >= len(charList):
            off_set = off_set % len(charList)
        out += charList[off_set]

    return out + "\n"


if __name__ == "__main__":
    file_name = "CPNT-216"

    with open(file_name, "a") as new_file:
        with open("sample.ini", "r") as file:
            for x in file.readlines():
                new_file.write(cipher(x))
