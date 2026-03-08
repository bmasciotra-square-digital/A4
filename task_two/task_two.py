from Crypto.Random import get_random_bytes

from aes.aes import encrypt, decrypt
from bbs.bbs import blum_blum_shub, generate_prime


def task_two():
    print("----- Task 2 -----")
    iv = get_random_bytes(16)

    p = generate_prime()
    q = generate_prime()

    key = blum_blum_shub(p, q, 256).to_bytes(32, byteorder='big')

    message = "hello world"

    encrypted = encrypt(message, key, iv)
    print(f"{encrypted=}")

    decrypted = decrypt(encrypted, key, iv)
    print(f"{decrypted=}")