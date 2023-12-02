#!usr/bin/env python3
# -*- coding: ascii -*-

import sys

def encrypt(realText, step):
    result = ""

    for i in range(len(realText)):
        char = realText[i]

        if (char.isupper()):
            result += chr((ord(char) - 1 + step - 64) % 26 + 65)

        else:
            result += chr((ord(char) - 1 + step - 96) % 26 + 97)
    return result

def decrypt(realText, step):
    result = ""

    for i in range(len(realText)):
        char = realText[i]

        if (char.isupper()):
            result += chr((ord(char) - 1 - step - 64) % 26 + 65)

        else:
            result += chr((ord(char) - 1 - step - 96) % 26 + 97)
    return result

if __name__=="__main__":
    if len(sys.argv) == 1:
        print("How to use: python3 caesar.py [-E, -D] string numeralkey")

    else:
        if sys.argv[1] == "-E":
            print(f"output: {encrypt(sys.argv[2], int(sys.argv[3]))}")

        elif sys.argv[1] == "-D":
            print(f"output: {decrypt(sys.argv[2], int(sys.argv[3]))}")

        else:
            print("How to use: python3 caesar.py [-E, -D] string numeralkey")

