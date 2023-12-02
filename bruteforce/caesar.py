#!usr/bin/env python3
# -*- coding: ascii -*-
import sys

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def bruteforce(message):
    for key in range(len(LETTERS)):
        translated = ''

        for symbol in message:
            if symbol in LETTERS:
                num = LETTERS.find(symbol)
                num = num - key

                if num < 0:
                    num = num + len(LETTERS)
                translated = translated + LETTERS[num]

            else:
                translated = translated + symbol

        print(f'trying key #{key}, {translated}')



if __name__=="__main__":
    if len(sys.argv) == 1:
        print("How to use: python3 caesarBruteForce.py string")

    elif len(sys.argv) == 2:
        bruteforce(sys.argv[1].upper())




