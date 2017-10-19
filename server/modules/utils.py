import time
import hashlib


def encrypt_password(password, email):
    _hash = hashlib.md5()
    _hash.update(password.encode('utf-8'))
    _hash.update(email.encode('utf-8'))
    return _hash.hexdigest()


def create_register_link(email, password, salt):
    _hash = hashlib.blake2b()
    _hash.update(email.encode('utf-8'))
    _hash.update(password.encode('utf-8'))
    _hash.update(salt.encode('utf-8'))
    _hash.update(str(time.time()).encode('utf-8'))
    return _hash.hexdigest()[:50]
