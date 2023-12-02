r/bin/env python3
# -*- coding: ascii -*-
import sys

def encrypt(rows, plaintext):
    assert len(plaintext) % rows == 0

    n = len(plaintext)
    columns = n // rows
    ciphertext = ['-'] * n

    for i in range(n):
        row = i // columns
        col = i % columns
        ciphertext[col * rows + row] = plaintext[i]

    return "".join(ciphertext)

def decrypt(rows, ciphertext):
    assert len(ciphertext) % rows == 0

    return encrypt(len(ciphertext) // rows, ciphertext)

if __name__=="__main__":
    if len(sys.argv) == 1:
        print("How to use: python3 scytale.py [-E, -D] string rows")

    else:
        if sys.argv[1] == "-E":
            print(f"output: {encrypt(int(sys.argv[3]), sys.argv[2])}")

        elif sys.argv[1] == "-D":
            print(f"output: {decrypt(int(sys.argv[3]), sys.argv[2])}")

        else:
            print("How to use: python3 scytale.py [-E, -D] string rows ")

