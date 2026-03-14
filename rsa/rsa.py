import secrets

from bbs.bbs import is_prime


def generate_rsa_prime() -> int:
    while True:
        # generate the random 1024 number
        candidate = secrets.randbits(1024)
        # force candidate to be 1024 bits - incase first bit is 0
        candidate |= (1 << 1023)
        # Enforce odd number
        candidate |= 1

        if is_prime(candidate):
            return candidate


class RSA:
    def __init__(self):
        self.n = None
        self.e = 65537
        self.d = None

    def generate_keys(self):
        p, q = self.select_primes()

        self.n = p * q
        phi_n = (p - 1) * (q - 1)

        self.d = pow(self.e, -1, phi_n)

    def encrypt(self, message):
        m = self.convert_string_to_int(message)
        return pow(m, self.e, self.n)

    def decrypt(self, ciphertext):
        m = pow(ciphertext, self.d, self.n)

        byte_length = (m.bit_length() + 7) // 8
        return m.to_bytes(byte_length, "big")

    def convert_string_to_int(self, message):
        if isinstance(message, bytes):
            return int.from_bytes(message, "big")

        if isinstance(message, str):
            return int.from_bytes(message.encode("utf-8"), "big")

        raise TypeError("Message must be str or bytes")

    def extended_euclidean_algorithm(self, a, b) -> int:

        row_index = -1
        x = [1, 0]
        y = [0, 1]

        while True:
            if row_index > 0:
                remainder = a % b
                quotient = a // b

                if remainder == 0:
                    return y[-1]

                x_i = x[row_index - 1] - quotient * x[row_index]
                y_i = y[row_index - 1] - quotient * y[row_index]

                x.append(x_i)
                y.append(y_i)

                a = b
                b = remainder

            row_index += 1

    def calculate_d(self, phi_n, e):
        e_inverse = self.extended_euclidean_algorithm(phi_n, e)
        return e_inverse % phi_n

    @staticmethod
    def select_primes() -> tuple[int, int]:
        while True:
            p = generate_rsa_prime()
            q = generate_rsa_prime()

            if p != q:
                return p, q
