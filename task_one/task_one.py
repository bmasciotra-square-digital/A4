from bbs.bbs import generate_prime, blum_blum_shub


def task_one():
    print("----- Task 1 -----")
    p = generate_prime()
    q = generate_prime()

    random = blum_blum_shub(p, q)
    print(f"{p=}")
    print(f"{q=}")
    print(f"{random=}")
