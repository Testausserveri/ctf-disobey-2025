from string import ascii_lowercase
from random import shuffle

cipher_mapping_lower = list(ascii_lowercase)
shuffle(cipher_mapping_lower)

cipher = dict(zip(str(ascii_lowercase), cipher_mapping_lower))


def encrypt(plain: str) -> str:
    return ''.join(cipher.get(char.lower()).upper() if char.isupper() else cipher.get(char, char) for char in plain)


plaintext = open("plaintext.txt").read()
output_file = open("ciphertext.txt", "x").write(encrypt(plaintext))

