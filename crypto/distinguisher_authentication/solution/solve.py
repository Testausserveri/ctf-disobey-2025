from pwn import process, remote
from random import randbytes


def solve_challenge(conn: process):
    conn.sendlineafter(b'> ', b'1')
    input = randbytes(16).hex()
    conn.sendlineafter(b'> ', input.encode())
    answer1 = conn.recvline().decode().strip()
    conn.sendlineafter(b'> ', b'1')
    conn.sendlineafter(b'> ', input.encode())
    answer2 = conn.recvline().decode().strip()
    distinguish = "1" if answer1 == answer2 else "0"
    conn.sendlineafter(b'> ', b'2')
    conn.sendlineafter(b'> ', distinguish.encode())

server_address = "127.0.0.1"
server_port = 5786
conn = remote(server_address, server_port)
# conn = process(["python3", "service.py"])
N = 100

for i in range(N):
    solve_challenge(conn)
    print(f"Challenge {i + 1} solved")
conn.recvuntil(b':\n')
flag = conn.recvline().decode().strip()
conn.recvall()
print(f"Flag is {flag}")

