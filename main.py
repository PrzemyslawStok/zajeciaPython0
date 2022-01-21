def funkcja1():
    for i in range(10):
        print(f"{i}")


def funkcja2(min: int, max: int):
    for i in range(min, max):
        print(f"{i ** 2}")


if __name__ == '__main__':
    print('PyCharm')

    funkcja1()
    funkcja2(0, 10)
