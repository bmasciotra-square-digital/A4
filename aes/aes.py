from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def encrypt(plaintext: str, key: bytes, iv: bytes) -> bytes:
    return AES.new(key=key, mode=AES.MODE_CBC, iv=iv).encrypt(pad(plaintext.encode(), AES.block_size))


def decrypt(ciphertext: bytes, key: bytes, iv: bytes) -> str:
    return unpad(AES.new(key=key, mode=AES.MODE_CBC, iv=iv).decrypt(ciphertext), AES.block_size).decode()
