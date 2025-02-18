#!/usr/local/bin/python3

from Crypto.Cipher import AES
from itertools import cycle, batched
from FLAG import FLAG
from os import urandom


def xor(a: bytes, b: bytes) -> bytes:
    return bytes([x ^ y for x, y in zip(a, b)])


def bitwise_and(a: bytes, b: bytes) -> bytes:
    return bytes([x & y for x, y in zip(a, b)])


def holy_hash(input: bytes) -> bytes:
    digest_len = 128
    x = input

    x = xor(x, cycle(b"MayGodBlessThisDigest"))
    x = xor(x, cycle(b"ThisIsAVeryHolyHash"))
    x = xor(x, cycle(b"CanIGetAnAmenForThisVeryHolyHash"))
    x = xor(x, cycle(b"ThisHashIsSoHolyItCannotBroken"))

    digest = 0
    iv = 0
    for block in map(lambda x: int.from_bytes(bytes(x), 'big'), batched(x, digest_len // 8)):
        cipher_block = pow(69, block ^ iv, 2**digest_len)  # CBC that shit!!
        iv = cipher_block
        digest ^= cipher_block

    return digest.to_bytes(digest_len // 8)


def encrypt_flag(key: bytes) -> tuple[bytes, bytes]:
    assert len(key) == 16
    cipher = AES.new(key, AES.MODE_CTR)
    enc_flag = cipher.encrypt(FLAG.encode())
    nonce = cipher.nonce
    return (enc_flag, nonce)


def decrypt_flag(key: bytes, nonce: bytes, encrypted_flag: bytes) -> bytes:
    assert len(key) == 16
    cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
    flag = cipher.decrypt(encrypted_flag)
    return flag


key = bitwise_and(urandom(16), b"\x1f" + 15 * b"\xff")

(enc_flag, nonce) = encrypt_flag(key)
hashed_key = holy_hash(key)
key = 16 * b'\x00'
print(f"HELLO. I AM THE SAFE. HERE'S THE HASHED KEY: {hashed_key.hex()}")
key_hex = input("GIVE ME THE KEY (hex).  > ")

user_key = bytes.fromhex(key_hex)
flag = decrypt_flag(user_key, nonce, enc_flag)

print("HERE'S THE SECRET YOU WANTED.")
print(flag.decode(errors='replace'))
exit(0)

