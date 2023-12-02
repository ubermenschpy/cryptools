#!usr/bin/env python3
# -*- coding: ascii -*-
import hashlib, cryptography, sys

if __name__=="__main__":
    if len(sys.argv) == 1:
        print("How to use: python3 hash.py string")

    elif len(sys.argv) == 2:
        for algorithm in hashlib.algorithms_guaranteed:
            print(algorithm)
            h = hashlib.new(algorithm)
            h.update(bytes(sys.argv[1], encoding="ascii"))

            try:
                print(h.hexdigest())

            except TypeError:
                print(h.hexdigest(128))
