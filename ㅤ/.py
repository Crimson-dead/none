"""###
    Tell me what else may I create. 
"""###
even = lambda value: value % 2 == 0


def func(value: int | float) -> bool:
    # just int or float into bool function 
    a: float = float()
    for i in range((value % 5) * value % 12):
        a += i % 7
        a *= i % 3
    return even(round(a))


all: tuple = tuple(range(1000))
passed: tuple = tuple(filter(func, all))

for j in passed: print(j)
