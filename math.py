even = lambda n: n % 2 == 0
square_of = lambda n: n ** 2
cube_of = lambda n: n ** 3
functions = (even, square_of, cube_of)


def main() -> None:
    for i in range(10):
        for func in functions:
            print(func(i))
        print()

if __name__ == '__main__':
    main()
