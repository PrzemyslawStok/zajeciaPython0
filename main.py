import numpy as np

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


if __name__ == '__main__':
    print('PyCharm')

    funkcja1()
    funkcja2(0, 10)

    powRange(10, 0, 10)

    array = np.arange(1,100)
    print(array)
    print(array**2)
