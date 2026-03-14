from bbs.bbs import generate_prime, blum_blum_shub
from rsa.rsa import RSA
from Crypto.Random import get_random_bytes


# uses the same RSA passed from Task 1
def task_three(rsa: RSA):
    # PT 1. Encrypt and decrypt example
    message = "hello world"
    encrypted = rsa.encrypt(message)

    print(f"{encrypted=}")

    decrypted = rsa.decrypt(encrypted)
    print(f"{decrypted=}")

    # PT 2. AES Encryption with RSA

    # Encrypt the AES symmetric key with the recipient’s RSA public key for secure
    # transmission over the network.

    p = generate_prime()
    q = generate_prime()

    aes_key = blum_blum_shub(p, q, 256).to_bytes(32, byteorder='big')

    aes_cipher = rsa.encrypt(aes_key)

    # PT.3 Decrypt with RSA

    # Use the recipient’s private key to decrypt the received AES key and confirm successful
    # retrieval.

    # the private key to the RSA class is an attribute under "d" that is used in the decrypt function
    aes_key_message = rsa.decrypt(aes_cipher)

    # Verify the decrypted value is equal to the generated aes key
    print(f"AES Key is the same as Decrypted: {aes_key_message == aes_key}")
