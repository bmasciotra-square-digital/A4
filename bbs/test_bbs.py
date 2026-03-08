import pytest
import math

from bbs.bbs import generate_prime, blum_blum_shub


@pytest.fixture
def setup():
    p = generate_prime()
    q = generate_prime()
    return blum_blum_shub(p, q)


@pytest.fixture
def large_prime():
    p = generate_prime()
    q = generate_prime()
    return blum_blum_shub(p, q, 2048)


def test_bbs_success(setup):
    assert setup.bit_length() >= 256


def test_bbs_success_large_bits():
    p = generate_prime()
    q = generate_prime()

    value = blum_blum_shub(p, q, 1024)

    assert value.bit_length() >= 1024


# NIST Tests
LOWER_RANGE = 0.45
UPPER_RANGE = 0.55


def test_monobit_test(setup):
    total_bits = setup.bit_length()
    ones = setup.bit_count()
    proportion = ones / total_bits

    assert LOWER_RANGE <= proportion <= UPPER_RANGE


def test_run(setup):
    n = setup.bit_length()
    bit_string = bin(setup)[2:]  # full binary string

    n1 = bit_string.count("1")
    n0 = n - n1

    # Basic sanity check
    if n < 2:
        return False

    # Count runs
    runs = 1
    for i in range(1, n):
        if bit_string[i] != bit_string[i - 1]:
            runs += 1

    # Expected runs
    mu = (2 * n0 * n1) / n + 1

    # Variance
    variance = (
            (2 * n0 * n1 * (2 * n0 * n1 - n))
            / (n ** 2 * (n - 1))
    )

    sigma = math.sqrt(variance)

    # Z-score
    z = (runs - mu) / sigma

    # 95% confidence threshold
    return abs(z) < 1.96


# Maurer Universal Statistical Test expected values and variances
# L | expected   | variance
# 1 | 0.7326495  | 0.690
# 2 | 1.5374383  | 1.338
# 3 | 2.4016068  | 1.901
# 4 | 3.3112247  | 2.358
# 5 | 4.2534266  | 2.705
# 6 | 5.2177052  | 2.954
# 7 | 6.1962507  | 3.125
def test_maurer_universal(large_prime, l: int = 3):
    """
    :param large_prime:
    :param l: the size of the block in which we are testing the pattern
    :return:
    """
    bit_string = format(large_prime, "02048b")
    n = len(bit_string)

    total_blocks = n // l
    q = 10 * (2 ** l)

    assert total_blocks > q, "Sequence too short for Maurer test"

    k = total_blocks - q

    blocks = [
        int(bit_string[i:i + l], 2)
        for i in range(0, total_blocks * l, l)
    ]

    # FIX: initialize with -1 instead of 0
    pattern_table = [-1] * (2 ** l)

    for i in range(q):
        pattern_table[blocks[i]] = i

    sum_log = 0.0

    for i in range(q, total_blocks):
        block = blocks[i]
        last = pattern_table[block]

        if last != -1:
            distance = i - last
            sum_log += math.log2(distance)

        pattern_table[block] = i

    fn = sum_log / k

    # Configure the variance and expected values based on the block length
    match l:
        case 1:
            expected, variance = 0.7326495, 0.690
        case 2:
            expected, variance = 1.5374383, 1.338
        case 3:
            expected, variance = 2.4016068, 1.901
        case 4:
            expected, variance = 3.3112247, 2.358
        case 5:
            expected, variance = 4.2534266, 2.705
        case 6:
            expected, variance = 5.2177052, 2.954
        case 7:
            expected, variance = 6.1962507, 3.125
        case _:
            raise ValueError(f"Unsupported block length l={l}")  # fallback

    sigma = math.sqrt(variance / k)
    z = (fn - expected) / sigma

    assert abs(z) < 1.96
