#!usr/bin/env python3
# -*- coding: ascii -*-
import sys

alphabet = "abcdefghijklmnopqrstuvwxyz "

letterToIndex = dict(zip(alphabet, range(len(alphabet))))
indexToLetter = dict(zip(range(len(alphabet)), alphabet))


def encrypt(message, key):
    encrypted = ""
    splitMessage = [
        message[i : i + len(key)] for i in range(0, len(message), len(key))
    ]

    for eachSplit in splitMessage:
        i = 0
        for letter in eachSplit:
            number = (letterToIndex[letter] + letterToIndex[key[i]]) % len(alphabet)
            encrypted += indexToLetter[number]
            i += 1

    return encrypted


def decrypt(cipher, key):
    decrypted = ""
    split_encrypted = [
        cipher[i : i + len(key)] for i in range(0, len(cipher), len(key))
    ]

    for each_split in split_encrypted:
        i = 0
        for letter in each_split:
            number = (letterToIndex[letter] - letterToIndex[key[i]]) % len(alphabet)
            decrypted += indexToLetter[number]
            i += 1

    return decrypted

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("How to use: python3 vigenere.py [-E, -D] string keyword")

    else:
        if sys.argv[1] == "-E":
            print(f"output: {encrypt(sys.argv[2], sys.argv[3])}")

        elif sys.argv[1] == "-D":
            print(f"output: {decrypt(sys.argv[2], sys.argv[3])}")

        else:
            print("How to use: python3 vigenere.py [-E, -D] string keyword ")

