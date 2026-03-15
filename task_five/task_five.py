import time

from rsa.rsa import RSA


def task_five(rsa: RSA):
    print("----- Task 5 -----")

    # CRT Implementation: [10]
    # Implement CRT to reduce computational overhead during RSA.
    # Demonstrate the speedup by running comparisons between standard RSA decryption and
    # CRT-optimized RSA decryption in your key exchange.

    message = "Cryptology is cool"
    long_message = "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of ' deFinibusBonorum et Malorum'(The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, 'Loremipsum dolorsitamet.., comes from a line in section 1.10.32.The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from ' de Finibus Bonorum etMalorum' by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.'"
    cipher = rsa.encrypt(message)
    long_cipher = rsa.encrypt(long_message)

    start = time.perf_counter()
    plaintext_crt = rsa.decrypt_crt(cipher)
    end = time.perf_counter()

    print("RSA CRT Decryption Time:", end - start, "seconds")

    start = time.perf_counter()
    long_plaintext_crt = rsa.decrypt_crt(long_cipher)
    end = time.perf_counter()

    print("Long CRT Decryption Time:", end - start, "seconds")

    start = time.perf_counter()
    long_plaintext_crt = rsa.decrypt(long_cipher)
    end = time.perf_counter()

    print("Long Decryption Time:", end - start, "seconds")

    print(f"message: \"{message}\" | cipher: {cipher} | plaintext: {plaintext_crt} | {message == plaintext_crt}")
