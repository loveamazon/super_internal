import hashlib


def hash_str(string):
    return hashlib.sha1(string).hexdigest()
