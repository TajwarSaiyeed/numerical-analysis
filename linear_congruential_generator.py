from typing import List


def linear_congruential_generator_fn(a, c, m_val, x0, num):
    sequence = [x0]
    x = x0
    for _ in range(1, num):
        x = (a * x + c) % m_val
        sequence.append(x)
    return sequence

def normalize_fn(gen: List[int], m_val: int) -> List[float]:
    return [float(x / m_val) for x in gen]


def check_repeatation(gen: List[int]) -> bool:
    return len(gen) != len(set(gen))



if __name__ == "__main__":
    m = 16
    generated = linear_congruential_generator_fn(5, 3, m, 1, 10)
    normalize = normalize_fn(generated, m)
    repeated = check_repeatation(generated)

    print("GENERATED : ", generated)
    print("NORMALIZED : ", normalize)
    print("REPEATED : ", repeated)