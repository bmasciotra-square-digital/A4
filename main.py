from bbs import bbs

if __name__ == '__main__':
    p = bbs.generate_prime()
    q = bbs.generate_prime()

    random = bbs.blum_blum_shub(p, q)
