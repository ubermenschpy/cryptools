#!usr/bin/env python3
# -*- coding: ascii -*-
import hashlib, sys


md5 = hashlib.md5()
sha1 = hashlib.sha1()
sha224 = hashlib.sha224()
sha256 = hashlib.sha256()
sha384 = hashlib.sha384()
sha512 = hashlib.sha512()

list_hash_objects = [md5, sha1, sha224, sha256, sha384, sha512]

if __name__=="__main__":
    if len(sys.argv) == 1:
        print("How to use: python3 hashfile.py path")

    elif len(sys.argv) == 2:
        path = fr'{sys.argv[1]}'
        for hash_object in list_hash_objects:
            with open(path, 'rb') as opened_file:
                for line in opened_file:
                    hash_object.update(line)
                print('{}: {}'.format(hash_object.name, hash_object.hexdigest()))

