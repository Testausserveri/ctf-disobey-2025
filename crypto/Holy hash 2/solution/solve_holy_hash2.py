from dlog import pohlig_hellman
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


server_address = "127.0.0.1"  # change into real server address
server_port = 5788
conn = pwn.remote(server_address, server_port)
# conn = pwn.process(["python3", "holy_hash2.py"])

conn.recvuntil(b": ")
hashed_key_hex = conn.recvline()[:-1].decode()
print(f"Hashed key is: {hashed_key_hex}")
hashed_key = int.from_bytes(bytes.fromhex(hashed_key_hex))
print(f"Hashed key in number form: {hashed_key}")

print(f"Now solving the equation: 69**x = {hashed_key} mod 2**128 using silver-pohlig-hellman")
dlog = pohlig_hellman(hashed_key, 69, 2**128, 2**126, [(2, 126)])
print(f"Solved discrete log and got the number: {dlog}")

key_before_xor = dlog.to_bytes(16)
key = make_xors(key_before_xor).hex()
print(f"Got key: {key}")

print("Sending key...")
conn.sendlineafter(b"  > ", key.encode())
conn.recvuntil(b"WANTED.\n")
flag = conn.recvline()

print("Got flag")
print(flag.decode())
conn.recvall()
