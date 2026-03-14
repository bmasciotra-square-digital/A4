from bbs.bbs import generate_prime, blum_blum_shub
from rsa.rsa import RSA, generate_rsa_prime


def task_one():
    print("----- Task 1 -----")

    # Step 1: generate BBS primes

    p_bbs = generate_prime()
    q_bbs = generate_prime()

    print("BBS primes:")
    print(f"{p_bbs=}")
    print(f"{q_bbs=}")

    # Step 2: generate BBS random bitstream (for NIST tests)
    bbs_output = blum_blum_shub(p_bbs, q_bbs, 4096)

    print("\nBBS output sample:")
    print(bbs_output)

    # Step 3: generate RSA key pair
    rsa = RSA()
    rsa.generate_keys()

    print("\nRSA Key Pair")
    print(f"n = {rsa.n}")
    print(f"e = {rsa.e}")
    print(f"d = {rsa.d}")

    # Return keys for later tasks
    return rsa
