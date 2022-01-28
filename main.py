import numpy as np
import timeit


def funkcja1():
    for i in range(10):
        print(f"{i}")


def funkcja2(min: int, max: int):
    for i in range(min, max):
        print(f"{i ** 2}")


# proszę napisać funkcję wyśwetlającą zdefiniowane potęgi liczb dla pewnego zagresu np. 5 potęgi liczb od 2 do 100.

def powRange(pow: int, min: int, max: int):
    for i in range(min, max):
        print(f"{i ** pow}")


# proszę napisać podobną funkcję przy pomocy biblioteki numpy

def powRange_numpy(pow: int, min: int, max: int):
    print(np.arange(min, max, dtype=np.float32) ** pow)


def arangeMatrix(min: int, max: int) -> list:
    A = []
    for i in range(min, max):
        A.append(i)
    return A


def arangeMatrixNumpy(min: int, max: int) -> np.ndarray:
    pass


if __name__ == '__main__':
    # A = [1,2,3,4,5,6]

    # print(A)
    # B = np.array([1,2,3,4,5,6])
    # print(B)
    # print(B+10)

    M = np.arange(1, 100_000_000, 2)
    print(M[10000])

    start_time = timeit.default_timer()
    arangeMatrix(0, 10_000_000)
    end_time = timeit.default_timer()
    print(f"arangeMatrix elapsed time: {(end_time - start_time):0.5f}s")
