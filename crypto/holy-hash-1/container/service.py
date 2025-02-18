#!/usr/local/bin/python3

from itertools import cycle, batched
from FLAG import FLAG


def xor(a: bytes, b: bytes) -> bytes:
    return bytes([x ^ y for x, y in zip(a, b)])


def holy_hash(input: bytes) -> bytes:
    digest_len = 128
    x = input

    x = xor(x, cycle(b"MayGodBlessThisDigest"))
    x = xor(x, cycle(b"ThisIsAVeryHolyHash"))
    x = xor(x, cycle(b"CanIGetAnAmenForThisVeryHolyHash"))
    x = xor(x, cycle(b"ThisHashIsSoHolyItCannotBroken"))

    digest = 0
    IV = 0
    for block in map(lambda x: int.from_bytes(bytes(x), 'big'), batched(x, digest_len // 8)):
        cipher_block = pow(69, block ^ IV, 2**digest_len)  # CBC that shit!!
        IV = cipher_block
        digest ^= cipher_block

    return digest.to_bytes(digest_len // 8)


print("Hi, welcome to our hash chuch! We worship our holy hash function by eating hashbrowns.")
print("Our holy hash function is so good and graceful!.")
print("We ascend by finding collision in holy_hash. Ff you find an collision you are seperated from us mortals into hashheaven.")
print("Can you ascend?")
x1_hex = input("Give me the first input (hex).  > ")
x2_hex = input("Give me the second input (hex).  > ")
x1 = bytes.fromhex(x1_hex)
x2 = bytes.fromhex(x2_hex)

if not x1 == x2 and holy_hash(x1) == holy_hash(x2):
    print(FLAG)
    print("You have ascended!")
else:
    print("Heretic!! I cannot accept this in my hashchurch!")

exit(0)

