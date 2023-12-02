# encoding: ascii
import sys, hashlib
from time import sleep

def bruteForce(hash, dic):
    finded = False
    # identify hashtype
    hashtype = hashlib

    if len(hash) == 32: #md5
        hashtype = hashlib.md5

    elif len(hash) == 56: #sha224
        hashtype = hashlib.sha224

    elif len(hash) == 40: #sha1
        hashtype = hashlib.sha1

    elif len(hash) == 64: #sha256
        hashtype = hashlib.sha256

    elif len(hash) == 96: #sha384
        hashtype = hashlib.sha384

    elif len(hash) == 128: #sha512
        hashtype = hashlib.sha_512

    try:
        pass_file = open(dic, "r")

        for word in pass_file:

            cipher_word = word.encode("ascii")

            hash_word = hashtype(cipher_word.strip())
            digest = hash_word.hexdigest()

            if digest == hash:
                print(f"hashes found!!!\nthe hashtype is: {hashtype.__name__}\nthe cipherword is: {word}")
                finded = True
                break

        if not finded:
            sleep(.8)
            print(f"Hash is not finded on the dic " + dic)

    except FileNotFoundError as e:
        print(e)


if __name__=="__main__":
    if len(sys.argv) != 3:
        print(f"how to use: python3 hashBruteForce.py <cipher_text> <dictionarie_path>\n\nExample python3 hashBruteForce.py 'a15f8b81a160b4eebe5c84e9e3b65c87b9b2f18e' './dict/bruteforce.txt'")
    else:
        bruteForce(sys.argv[1], sys.argv[2])
