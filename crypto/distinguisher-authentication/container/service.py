#!/usr/local/bin/python3

from typing import Optional
from os import urandom
from random import choice, randbytes
from Crypto.Cipher import AES

from FLAG import FLAG

def cipher(key: bytes, plain_text: bytes) -> bytes:
    assert len(key) <= 16
    aes = AES.new(key, AES.MODE_CTR, initial_value=b'\x1b' * 8,nonce=b'\x7f' * 8)
    return aes.encrypt(plain_text)

def ask_the_oracle(key: bytes, question: bytes, state: bool) -> bytes:
    if state:
        return cipher(key, question)
    else:
        return cipher(key, randbytes(len(question)))

def flip_coin() -> bool:
    return choice([False, True])
    

def str_to_bool(guess: str) -> Optional[bool]:
    if guess == "0":
        return False
    elif guess == "1":
        return True
    else:
        return None

def challenge() -> bool:
    state: bool = flip_coin()
    key: bytes = urandom(16)
    while True:

        print("1: Ask the Oracle a question \n2: Make a guess which oracle is it")
        option: str = input("> ").strip()

        if option == "1":
            question_hex: str = input("What do you want to ask from the oracle (hex) > ").strip()
            try:
                question: bytes = bytes.fromhex(question_hex)
            except ValueError:
                print("Invalid hex")
                exit(1)
            answer: bytes = ask_the_oracle(key, question, state)
            print(answer.hex())

        elif option == "2":
            guess_unparsed: str = input("Make a guess, Is the oracle a virus (0) or the real deal (1) > ").strip()
            guess: Optional[bool] = str_to_bool(guess_unparsed)
            if guess == None:
                print("Invalid guess")
                exit(1)
            
            return guess == state

        else:
            print("Invalid input")
            exit(1)

N: int = 100
print("User authentication sequence initiated...")
print("Loading detection...")
print(f"To authenticate please guess which oracle is in each of the {N} scenarios, the virus or the real oracle.")
print("When you ask the real oracle to encrypt, it encrypts it but the virus encrypts a random message of the same length.")

answers: list[bool] = []
for i in range(N):
    answers.append(challenge())
    print(f"Challenge {i + 1} completed!")

# Calculate advantage
wins: int = answers.count(True)
losses: int = answers.count(False)
adv: float = abs((wins / N) - (losses / N))

if adv >= 0.95:
    print("User authenticated :)")
    print("Here's the company secret:")
    print(FLAG)
else:
    print("User authentication failed :(")
    print("Please try again.")

exit(0)