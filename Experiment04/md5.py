# MD5
import hashlib

def md5_hash_string(input_string):
    md5_hash = hashlib.md5()
    md5_hash.update(input_string.encode('utf-8'))
    hex_digest = md5_hash.hexdigest()
    return hex_digest

input_string = input("Enter a string to hash using MD5: ")
md5_hash_string(input_string)
