# TASK 4 - Image Encryption Using AES and Client-to-Client Transmission
import imageio.v2 as iio
import matplotlib.pyplot as plt

from aes.aes import AES256
from rsa.rsa import RSA


def task_four(aes: AES256):
    print("----- Task 4 -----")

    # Encrypt an image file and send it securely between clients using the AES key generated and exchanged in
    # Tasks 2 and 3.

    # Show the Image
    img = iio.imread("task_four/tea.jpg")
    plt.imshow(img)
    plt.axis("off")
    plt.title("Original Image")
    plt.show()

    # 1. Image Encryption: [5]
    # Encrypt the image data using the AES key (use CBC mode for consistency with Task 2).

    # parse the image to file bytes to convert
    with open("task_four/tea.jpg", "rb") as f:
        image_bytes = f.read()
        # Bytes converted to cipher
        cipher = aes.encrypt(image_bytes)

        with open("task_four/cipher.jpg", "wb") as cf:
            cf.write(cipher)

        # 2. Transmission and Decryption: [10]
        # Simulate the transmission by saving the encrypted image data and decrypting it on the
        # receiver’s end.

        image_encrypted = aes.decrypt(cipher)

    # Write to a new file
    with open("task_four/tea_decrypted.jpg", "wb") as f:
        f.write(image_encrypted)

    img = iio.imread("task_four/tea_decrypted.jpg")
    plt.imshow(img)
    plt.axis("off")
    plt.title("Decrypted Image")
    plt.show()
