import time

from rsa.rsa import RSA


def task_five(rsa: RSA):
    print("----- Task 5 -----")

    # CRT Implementation: [10]
    # Implement CRT to reduce computational overhead during RSA.
    # Demonstrate the speedup by running comparisons between standard RSA decryption and
    # CRT-optimized RSA decryption in your key exchange.

    message = "Cryptology is cool"
    cipher = rsa.encrypt(message)

    start = time.perf_counter()
    plaintext_crt = rsa.decrypt_crt(cipher)
    end = time.perf_counter()
    print("RSA CRT Decryption Time:", end - start, "seconds")

    print(f"message: \"{message}\" | cipher: {cipher} | plaintext: {plaintext_crt} | {message == plaintext_crt}")
    pass
