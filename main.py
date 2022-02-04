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
    return np.arange(min, max)

def zad1():
    A = np.array([[1,2,3,4,5],[6,7,8,9,10]])
    B = np.array([[1,2],[2,3],[4,5],[6,7],[8,9]])

    print(A)
    print(B)

    print(A.T)

    #proszę obliczyć (A.T+(2B+A.T).T).T

    pass


if __name__ == '__main__':
    # A = [1,2,3,4,5,6]

    # print(A)
    # B = np.array([1,2,3,4,5,6])
    # print(B)
    # print(B+10)

    M = np.arange(1, 100_000_000, 2)

    min = 0
    max = 10_000_000

    start_time = timeit.default_timer()
    arangeMatrix(min, max)
    end_time = timeit.default_timer()
    print(f"arangeMatrix elapsed time: {(end_time - start_time):0.5f}s")

    start_time = timeit.default_timer()
    arangeMatrixNumpy(min, max)
    end_time = timeit.default_timer()
    print(f"arangeMatrixNumpy elapsed time: {(end_time - start_time):0.5f}s")

    A = np.arange(1,100)

    zad1()