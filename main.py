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
    A = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
    B = np.array([[1, 2], [2, 3], [4, 5], [6, 7], [8, 9]])

    # print(A)
    print(B)

    # print(A.T)

    print(2 * B)

    # proszę obliczyć (A.T+(2B+A.T)).T

    print((A.T + (2 * B + A.T)).T)


def zad2():
    # proszę utworzyć macierz A o rozmiarze [20,1000] składającą się z losowych cyfr
    # proszę utworzyć macierz B o rozmiarze [1000,20] wypełnioną kolejnymi cyframi

    # proszę rozwiązać 5*(A.T+B)+1000*(B.T+A).T

    print(np.random.randint(0, 5, [5, 5]))
    print(np.arange(0, 100).reshape([10, -1]))

    A = np.random.randint(0, 5, [20, 1000])
    B = np.arange(0, 1000 * 20).reshape([1000, -1])

    print(5 * (A.T + B) + 1000 * (B.T + A).T)


def zad3():
    A = np.random.randint(0, 5, [5, 5])
    B = 2 * np.ones([5, 5])

    # print(A)
    # print(B)

    # print(A * B)
    # print(np.dot(A, B))

    # proszę utworzyć macierz A o rozmiarze [50,100] składającą się z losowych cyfr od 1 do 10
    # proszę utworzyć macierz B o rozmiarze [100,50] wypełnioną kolejnymi cyframi

    # proszę rozwiązać (A.T*B).T+10*A

    A = np.random.randint(1, 10, [50, 100])
    B = np.arange(0, 100 * 50).reshape([100, -1])

    print((A.T * B).T + 10 * A)


def zad4():
    # proszę utworzyć macierz A o rozmiarze [500,100] składającą się z losowych cyfr od 10 do 20
    # proszę utworzyć macierz B o rozmiarze [100,500] wypełnioną kolejnymi cyframi

    A = np.random.randint(10, 20, [500, 100])
    B = np.arange(0, 100 * 500).reshape([100, -1])

    # proszę rozwiązać A^10+B.T^10
    pass


def zad5():
    # proszę utworzyć macierz A o rozmiarze [250,10] składającą się z losowych cyfr od 10 do 20
    # proszę utworzyć macierz B o rozmiarze [10,250] wypełnioną kolejnymi cyframi

    # proszę rozwiązać (A.T+B)*(2*B.T+10A)
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

    A = np.arange(1, 100)

    # zad1()
    # zad2()
    # zad3()
    zad4()