def add(val1: int, val2: int) -> int:
    return val1 + val2


def sub(val1: int, val2: int) -> int:
    return val1 - val2


def multiply(val1: int, val2: int) -> int:
    return val1 * val2


def divide(val1: int, val2: int) -> float:
    if val2 == 0:
        raise ZeroDivisionError()
    return val1 / val2
