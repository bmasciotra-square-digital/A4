from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


class AES256:
    def __init__(self, key, iv):
        self.k = key
        self.iv = iv

    def encrypt(self, plaintext: bytes) -> bytes:
        return AES.new(key=self.k, mode=AES.MODE_CBC, iv=self.iv).encrypt(pad(plaintext, AES.block_size))

    def decrypt(self, ciphertext: bytes) -> bytes:
        return unpad(AES.new(key=self.k, mode=AES.MODE_CBC, iv=self.iv).decrypt(ciphertext), AES.block_size)
