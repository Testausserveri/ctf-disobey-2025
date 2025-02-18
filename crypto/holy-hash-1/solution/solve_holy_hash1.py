from Crypto.Util.number import long_to_bytes
from itertools import cycle
import pwn


def xor(a: bytes, b: bytes) -> bytes:
    return bytes([x ^ y for x, y in zip(a, b)])


def make_xors(y: bytes) -> bytes:
    x = y
    x = xor(x, cycle(b"MayGodBlessThisDigest"))
    x = xor(x, cycle(b"ThisIsAVeryHolyHash"))
    x = xor(x, cycle(b"CanIGetAnAmenForThisVeryHolyHash"))
    x = xor(x, cycle(b"ThisHashIsSoHolyItCannotBroken"))
    return x


def gen_coll() -> tuple[bytes, bytes]:
    digestlen = 128
    eulerphi = 2**(digestlen - 1)  # or actually the order of 69 is carmichael(2**128) = 2**126 so 2**(digestlen-2) also works
    x1_pre_xor = long_to_bytes(1)
    x2_pre_xor = long_to_bytes(eulerphi + 1)
    x1 = make_xors(x1_pre_xor)
    x2 = make_xors(x2_pre_xor)
    return (x1, x2)


server_address = "127.0.0.1"  # Change into real server address
server_port = 5787
conn = pwn.tubes.remote.remote(server_address, server_port)
# conn = pwn.tubes.process.process(["python3", "holy_hash1.py"])

(x1, x2) = gen_coll()
print(x1.hex())
print(x2.hex())

conn.sendlineafter(b".  > ", x1.hex().encode())
conn.sendlineafter(b".  > ", x2.hex().encode())
flag = conn.recvuntil(b"]")
print(flag)
conn.recvall()
