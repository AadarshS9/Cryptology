#SHA1
import hashlib

def sha1_hash_string(input_string):
    sha1_hash = hashlib.sha1()
    sha1_hash.update(input_string.encode('utf-8'))
    hex_digest = sha1_hash.hexdigest()
    return hex_digest

input_string = input("Enter a string to hash using SHA-1: ")
sha1_hash_string(input_string)
