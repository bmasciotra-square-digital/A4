import secrets

MODULUS = 4
EXPECTED_REMAINDER = 3
RELATIVELY_PRIME = 1


def miller_rabin_test(d, n):
    a = secrets.randbelow(n - 3) + 2
    x = pow(a, d, n)

    if x == 1 or x == n - 1:
        return True

    while d != n - 1:
        x = (x * x) % n
        d *= 2

        if x == 1:
            return False
        if x == n - 1:
            return True

    return False


def is_prime(n, k=40):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    d = n - 1

    while d % 2 == 0:
        d //= 2

    for _ in range(k):
        if not miller_rabin_test(d, n):
            return False

    return True


def is_congruent_mod_four(value: int) -> bool:
    return value % MODULUS == EXPECTED_REMAINDER


def generate_prime(bbs_bits = 256) -> int:
    generated = secrets.randbits(bbs_bits)

    # Force 256-bit length
    generated |= (1 << (bbs_bits - 1))

    # Force odd
    generated |= 1

    if is_congruent_mod_four(generated) and is_prime(generated):
        return generated

    return generate_prime()


def euclidean_algorithm(x: int, y: int) -> int:
    if y == 0:
        return x

    return euclidean_algorithm(y, x % y)


def generate_seed(n: int) -> int:
    while True:
        s = secrets.randbelow(n)

        if s > 1 and euclidean_algorithm(s, n) == 1:
            return s


def blum_blum_shub(p: int, q: int, bit_count=256) -> int:
    # p and q MUST adhere to the following:
    # 1. Be prime numbers
    # 2. Be at least 256 bits
    # 3. Satisfy =>  p and q are congruent modulo to 3 mod 4 ie they have 3 remainder when divided by 4

    n = p * q
    seed = generate_seed(n)

    candidate = ""  # force to 256 bits
    x = pow(seed, 2, n)

    for _ in range(bit_count):
        x = pow(x, 2, n)
        candidate += str(x % 2)

    result = int(candidate, 2)
    result |= (1 << (bit_count - 1))  # force 256-bit output

    return result
